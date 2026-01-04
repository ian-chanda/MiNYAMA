# Minyama_Active_Inference_Model/src/inference_engine/world_model.py

"""
The WorldModel is the central, predictive component of the Active Inference
system. It maintains a generative model of the environment, represented as a
graph, and uses it to predict future states and select actions that minimize
surprise.
"""

from Minyama_Active_Inference_Model.src.data_model import (
    graph_representation,
    human_state_tensors,
    extraction_flows,
    baseline_model
)
from Minyama_Active_Inference_Model.src.inference_engine import surprise_calculator

class WorldModel:
    """
    A generative model of the environment used for active inference.
    """

    def __init__(self, system_graph):
        """
        Initializes the WorldModel with a system graph.

        Args:
            system_graph: A graph object from the graph_representation module.
        """
        self.system_graph = system_graph
        self.current_state = self._initialize_state_from_graph()
        print("WorldModel initialized.")

    def _initialize_state_from_graph(self):
        """Initializes the model's state from the system graph."""
        if self.system_graph:
            return {node: self.system_graph.nodes[node] for node in self.system_graph.nodes}
        return {}

    def predict_future_state(self, action):
        """
        Predicts the most likely future state of the world if a given
        action is taken.

        Args:
            action: The action to be simulated.

        Returns:
            A representation of the predicted future state.
        """
        print(f"  (WorldModel) Predicting future state for action: '{action}'...")
        # Placeholder: This logic would be complex. It would involve:
        # 1. Copying the current state.
        # 2. Applying the action's expected effects based on the graph dynamics.
        # 3. Returning the new, hypothetical state.
        predicted_state = self.current_state.copy()
        # Simulate a simple effect
        if action == "increase_resource_flow_X" and "resource_X" in predicted_state:
            predicted_state["resource_X"]["flow"] += 10
        elif action == "probe_system_with_diagnostic_query":
            predicted_state["system_awareness"] = predicted_state.get("system_awareness", 0.5) + 0.1

        return predicted_state

    def simulate_outcomes(self, possible_actions, inferred_goal):
        """
        Simulates the outcomes of possible actions to see which one best
        achieves an inferred goal. Used by the InverseAgency module.

        Args:
            possible_actions: A list of actions to simulate.
            inferred_goal: The goal to be achieved.

        Returns:
            The action that is most likely to achieve the goal.
        """
        print(f"  (WorldModel) Simulating outcomes for goal: '{inferred_goal}'...")
        # Placeholder: A simple simulation.
        if inferred_goal == "Resource Hoarding":
            # Find an action that increases a resource.
            for action in possible_actions:
                if "increase" in action and "flow" in action:
                    return action
        return possible_actions[0] # Default to first action

    def update_model(self, sensory_input, surprise_score):
        """
        Updates the internal model based on new sensory input and the
        calculated surprise. This is the "learning" part of the loop.

        Args:
            sensory_input: The new data from the environment.
            surprise_score: The degree of prediction error from the surprise calculator.
        """
        print(f"\n(WorldModel) Updating model with new sensory input and surprise score of {surprise_score}...")
        # Placeholder: If surprise is high, the model needs to be adjusted.
        # This could involve:
        # - Modifying edge weights in the graph.
        # - Adding or removing nodes/edges.
        # - Updating the baseline model.
        if surprise_score > 0.8: # Arbitrary high-surprise threshold
            print("  - High surprise detected! Triggering model adaptation...")
            # Example adaptation: adjust a node's property based on input
            for key, value in sensory_input.items():
                if key in self.current_state:
                    print(f"    - Updating state for '{key}' based on new input.")
                    self.current_state[key] = value

        print("  - Model update complete.")


# Example Usage
if __name__ == '__main__':
    # 1. Create a graph
    mock_graph = graph_representation.create_mock_graph()
    mock_graph.nodes["resource_X"]["flow"] = 50

    # 2. Initialize the model
    wm = WorldModel(system_graph=mock_graph)
    print(f"Initial state: {wm.current_state}")

    # 3. An action is chosen (by the objective function)
    action_to_take = "increase_resource_flow_X"
    predicted_state = wm.predict_future_state(action_to_take)
    print(f"Predicted state: {predicted_state}")

    # 4. New sensory input arrives, which is different from the prediction
    sensory_input = {"resource_X": {"flow": 75}} # Higher than predicted
    actual_state = sensory_input

    # 5. Surprise is calculated
    surprise = surprise_calculator.calculate_realized_surprise(predicted_state, actual_state)

    # 6. The model is updated based on the surprise
    wm.update_model(sensory_input, surprise)
    print(f"Updated state: {wm.current_state}")
