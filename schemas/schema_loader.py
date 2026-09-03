"""
MiNYAMA Schema Loader
---------------------
Utility module for loading, exploring, and visualizing the MiNYAMA sector
graph schemas in Jupyter Notebooks.

Usage:
    from schema_loader import MiNYAMAExplorer
    exp = MiNYAMAExplorer()
    exp.list_sectors()
    exp.sector_summary("agriculture")
    exp.node_df("agriculture")
    exp.edge_df("agriculture")
    exp.belief_df("agriculture")
    exp.plot_graph("agriculture")
"""

import json
import os
from pathlib import Path
from typing import Optional

SECTORS = ["agriculture", "education", "finance", "healthcare", "manufacturing", "retail"]
SECTOR_LABELS = {
    "agriculture": "Agriculture",
    "education": "Education",
    "finance": "Finance",
    "healthcare": "Healthcare",
    "manufacturing": "Manufacturing",
    "retail": "Retail",
}
SECTOR_ICONS = {
    "agriculture": "\U0001f33e",
    "education": "\U0001f4da",
    "finance": "\U0001f4b0",
    "healthcare": "\U0001f3e5",
    "manufacturing": "\U0001f3ed",
    "retail": "\U0001f6d2",
}


class MiNYAMAExplorer:
    """Interactive explorer for MiNYAMA sector graph schemas."""

    def __init__(self, base_path: Optional[str] = None):
        if base_path is None:
            base_path = str(Path(__file__).parent)
        self.base_path = Path(base_path)
        self._cache = {}

    # ------------------------------------------------------------------
    # Loading
    # ------------------------------------------------------------------
    def _load_export(self) -> dict:
        if "export" not in self._cache:
            export_path = self.base_path / "schemas_export.json"
            with open(export_path) as f:
                self._cache["export"] = json.load(f)
        return self._cache["export"]

    def _load_sector(self, sector: str) -> dict:
        if sector not in self._cache:
            export = self._load_export()
            self._cache[sector] = export["sectors"][sector]
        return self._cache[sector]

    # ------------------------------------------------------------------
    # Basic queries
    # ------------------------------------------------------------------
    def list_sectors(self):
        """Print all available sectors."""
        data = self._load_export()
        print("MiNYAMA Sectors:")
        print("-" * 50)
        for s in SECTORS:
            g = data["sectors"].get(s, {})
            n_nodes = len(g.get("nodes", []))
            n_edges = len(g.get("edges", []))
            icon = SECTOR_ICONS.get(s, "")
            print(f"  {icon} {SECTOR_LABELS[s]:<16} | {n_nodes:>3} nodes  {n_edges:>3} edges")
        return list(data["sectors"].keys())

    def sector_summary(self, sector: str):
        """Print a summary of a sector's graph schema."""
        g = self._load_sector(sector)
        icon = SECTOR_ICONS.get(sector, "")
        print(f"{icon} {SECTOR_LABELS[sector]} Sector Graph")
        print("=" * 60)
        print(f"  Schema ref:   {g.get('schema_ref', 'N/A')}")
        print(f"  Description:  {g.get('description', 'N/A')[:80]}...")
        print()

        meta = g.get("meta", {})
        print("  Node types:")
        for nt in meta.get("node_types", []):
            print(f"    - {nt}")
        print()
        print("  Edge types:")
        for et in meta.get("edge_type_enum", []):
            print(f"    - {et}")
        print()
        print(f"  Total nodes: {len(g.get('nodes', []))}")
        print(f"  Total edges: {len(g.get('edges', []))}")

        beliefs = [n for n in g.get("nodes", []) if n.get("beliefs")]
        observations = [n for n in g.get("nodes", []) if n.get("is_observation")]
        print(f"  Nodes with beliefs: {len(beliefs)}")
        print(f"  Observation nodes:  {len(observations)}")

    # ------------------------------------------------------------------
    # DataFrame helpers
    # ------------------------------------------------------------------
    def node_df(self, sector: str):
        """Return a pandas DataFrame of all nodes in a sector."""
        import pandas as pd
        g = self._load_sector(sector)
        rows = []
        for n in g.get("nodes", []):
            attrs = n.get("attributes", {})
            attr_flat = {k: v.get("value", v) for k, v in attrs.items()}
            rows.append({
                "id": n["id"],
                "type": n["type"],
                "has_beliefs": bool(n.get("beliefs")),
                "is_observation": n.get("is_observation", False),
                **{f"attr_{k}": v for k, v in attr_flat.items()},
            })
        return pd.DataFrame(rows)

    def edge_df(self, sector: str):
        """Return a pandas DataFrame of all edges in a sector."""
        import pandas as pd
        g = self._load_sector(sector)
        rows = []
        for e in g.get("edges", []):
            rows.append({
                "from": e["from"],
                "to": e["to"],
                "type": e["type"],
                "weight": e.get("weight", 1.0),
                "prior": e.get("prior", "unknown"),
            })
        return pd.DataFrame(rows)

    def belief_df(self, sector: str):
        """Return a pandas DataFrame of all beliefs across nodes."""
        import pandas as pd
        g = self._load_sector(sector)
        rows = []
        for n in g.get("nodes", []):
            for bname, bdef in n.get("beliefs", {}).items():
                btype = bdef.get("type", "unknown")
                params = bdef.get("params", {})
                confidence = bdef.get("confidence", None)
                rows.append({
                    "node_id": n["id"],
                    "node_type": n["type"],
                    "belief_name": bname,
                    "belief_type": btype,
                    "params": str(params),
                    "confidence": confidence,
                })
        return pd.DataFrame(rows)

    def node_type_counts(self, sector: str):
        """Return a pandas Series of node type counts."""
        import pandas as pd
        df = self.node_df(sector)
        return df["type"].value_counts()

    def edge_type_counts(self, sector: str):
        """Return a pandas Series of edge type counts."""
        import pandas as pd
        df = self.edge_df(sector)
        return df["type"].value_counts()

    # ------------------------------------------------------------------
    # Graph visualization (pyvis or matplotlib fallback)
    # ------------------------------------------------------------------
    def plot_graph(self, sector: str, height="600px", width="100%"):
        """Render the sector graph as an interactive HTML widget or matplotlib."""
        try:
            return self._plot_pyvis(sector, height, width)
        except ImportError:
            return self._plot_matplotlib(sector)

    def _plot_pyvis(self, sector: str, height: str, width: str):
        from pyvis.network import Network
        g = self._load_sector(sector)
        icon = SECTOR_ICONS.get(sector, "")
        net = Network(height=height, width=width, notebook=True, bgcolor="#1a1a2e", font_color="white")
        net.set_title(f"{icon} {SECTOR_LABELS[sector]} - Active Inference Graph")

        color_map = {
            "Zone": "#4CAF50", "Crop": "#8BC34A", "Equipment": "#795548",
            "Intervention": "#FF9800", "EnvironmentalData": "#03A9F4", "Yield": "#FFEB3B",
            "Learner": "#9C27B0", "KnowledgeConcept": "#E91E63", "LearningResource": "#00BCD4",
            "LearningInteraction": "#FF5722", "MasteryState": "#673AB7", "Assessment": "#F44336",
            "EconomicAgent": "#2196F3", "Asset": "#CDDC39", "Transaction": "#FFC107",
            "Market": "#3F51B5",
            "Patient": "#E91E63", "Provider": "#009688", "Encounter": "#FF5722",
            "HealthState": "#673AB7",
            "PhysicalAsset": "#795548", "Material": "#FFEB3B", "WorkOrder": "#FF9800",
            "Process": "#4CAF50", "SupplyChainLink": "#03A9F4",
            "Customer": "#9C27B0", "Product": "#8BC34A", "InventoryItem": "#795548",
            "CustomerInteraction": "#FF5722", "DemandForecast": "#3F51B5",
        }

        for n in g.get("nodes", []):
            node_type = n["type"]
            color = color_map.get(node_type, "#9E9E9E")
            label = n["id"]
            belief_count = len(n.get("beliefs", {}))
            title_lines = [f"<b>{n['id']}</b>", f"Type: {node_type}"]
            if n.get("is_observation"):
                title_lines.append("<i>Observation node</i>")
            if belief_count:
                title_lines.append(f"Beliefs: {belief_count}")
            for bname, bdef in n.get("beliefs", {}).items():
                title_lines.append(f"  {bname}: {bdef.get('type', '?')} (conf={bdef.get('confidence', '?')})")
            title = "<br>".join(title_lines)
            size = 15 + belief_count * 5
            net.add_node(n["id"], label=label, color=color, title=title, size=size)

        for e in g.get("edges", []):
            color = "#555555"
            if e.get("prior") == "deterministic":
                color = "#AAAAAA"
            elif e.get("prior") == "learned":
                color = "#FF6B35"
            title = f"{e['type']} (w={e.get('weight', 1.0):.2f}, {e.get('prior', '?')})"
            net.add_edge(e["from"], e["to"], label=e["type"], color=color, title=title, width=e.get("weight", 1.0) * 3)

        net.show(f"{sector}_graph.html")
        print(f"Rendered: {sector}_graph.html")
        return net

    def _plot_matplotlib(self, sector: str):
        import matplotlib.pyplot as plt
        import networkx as nx
        g = self._load_sector(sector)
        G = nx.DiGraph()
        for n in g.get("nodes", []):
            G.add_node(n["id"], node_type=n["type"], is_observation=n.get("is_observation", False))
        for e in g.get("edges", []):
            G.add_edge(e["from"], e["to"], edge_type=e["type"], weight=e.get("weight", 1.0))

        color_map = {
            "Zone": "#4CAF50", "Crop": "#8BC34A", "Equipment": "#795548",
            "Intervention": "#FF9800", "EnvironmentalData": "#03A9F4", "Yield": "#FFEB3B",
            "Learner": "#9C27B0", "KnowledgeConcept": "#E91E63", "LearningResource": "#00BCD4",
            "LearningInteraction": "#FF5722", "MasteryState": "#673AB7", "Assessment": "#F44336",
            "EconomicAgent": "#2196F3", "Asset": "#CDDC39", "Transaction": "#FFC107",
            "Market": "#3F51B5",
            "Patient": "#E91E63", "Provider": "#009688", "Encounter": "#FF5722",
            "HealthState": "#673AB7",
            "PhysicalAsset": "#795548", "Material": "#FFEB3B", "WorkOrder": "#FF9800",
            "Process": "#4CAF50", "SupplyChainLink": "#03A9F4",
            "Customer": "#9C27B0", "Product": "#8BC34A", "InventoryItem": "#795548",
            "CustomerInteraction": "#FF5722", "DemandForecast": "#3F51B5",
        }

        node_colors = [color_map.get(G.nodes[n].get("node_type", ""), "#9E9E9E") for n in G.nodes()]
        fig, ax = plt.subplots(figsize=(14, 10))
        pos = nx.spring_layout(G, k=2.0, iterations=50, seed=42)
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=800, alpha=0.9, ax=ax)
        nx.draw_networkx_labels(G, pos, font_size=8, font_color="white", font_weight="bold", ax=ax)
        nx.draw_networkx_edges(G, pos, edge_color="#888888", arrows=True, arrowsize=12, alpha=0.6, ax=ax)
        edge_labels = {(e[0], e[1]): e[2].get("edge_type", "")[:12] for e in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6, font_color="#666666", ax=ax)

        icon = SECTOR_ICONS.get(sector, "")
        ax.set_title(f"{icon} {SECTOR_LABELS[sector]} - Active Inference Graph", fontsize=14, fontweight="bold")
        ax.axis("off")
        plt.tight_layout()
        plt.show()
        return G

    # ------------------------------------------------------------------
    # Belief visualization
    # ------------------------------------------------------------------
    def plot_belief_distributions(self, sector: str, node_id: Optional[str] = None):
        """Plot probability distributions for beliefs in a sector."""
        import matplotlib.pyplot as plt
        import numpy as np
        from scipy import stats

        g = self._load_sector(sector)
        nodes = g.get("nodes", [])
        if node_id:
            nodes = [n for n in nodes if n["id"] == node_id]

        beliefs_to_plot = []
        for n in nodes:
            for bname, bdef in n.get("beliefs", {}).items():
                if bdef.get("type") == "Normal":
                    beliefs_to_plot.append((n["id"], bname, bdef))

        if not beliefs_to_plot:
            print("No Normal-distribution beliefs found to plot.")
            return

        n_plots = len(beliefs_to_plot)
        cols = min(3, n_plots)
        rows = (n_plots + cols - 1) // cols
        fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
        if n_plots == 1:
            axes = [axes]
        else:
            axes = axes.flatten() if hasattr(axes, 'flatten') else list(axes)

        for i, (nid, bname, bdef) in enumerate(beliefs_to_plot):
            ax = axes[i]
            params = bdef["params"]
            mean_vals = [v for k, v in params.items() if k.startswith("mean")]
            std_vals = [v for k, v in params.items() if k.startswith("std")]
            if mean_vals and std_vals:
                mu, sigma = mean_vals[0], std_vals[0]
                if sigma > 0:
                    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 200)
                    y = stats.norm.pdf(x, mu, sigma)
                    ax.plot(x, y, linewidth=2)
                    ax.fill_between(x, y, alpha=0.2)
                    ax.axvline(mu, color="red", linestyle="--", alpha=0.7, label=f"mu={mu:.2f}")
                    ax.set_title(f"{nid}.{bname}", fontsize=9)
                    ax.set_ylabel("density")
                    ax.legend(fontsize=7)
                else:
                    ax.text(0.5, 0.5, "sigma=0", ha="center", va="center", transform=ax.transAxes)
                    ax.set_title(f"{nid}.{bname}", fontsize=9)
            else:
                param_names = list(params.keys())
                param_vals = list(params.values())
                ax.bar(param_names, param_vals, color="#4A90D9", alpha=0.7)
                ax.set_title(f"{nid}.{bname}", fontsize=9)
                ax.tick_params(axis="x", rotation=45)

        for j in range(i + 1, len(axes)):
            axes[j].set_visible(False)

        icon = SECTOR_ICONS.get(sector, "")
        fig.suptitle(f"{icon} {SECTOR_LABELS[sector]} Belief Distributions", fontsize=13, fontweight="bold")
        plt.tight_layout()
        plt.show()
