import openai
import streamlit as st

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

# Function to generate workout and diet plans using GPT-3
def generate_fitness_plan(height, weight, fitness_goal):
    prompt = f"Create a personalized workout and diet plan for an individual with the following characteristics:\n\n\
- Height: {height} cm\n\
- Weight: {weight} kg\n\
- Fitness Goal: {fitness_goal}\n\n\
Consider the following details when providing the plans:\n\n\
1. **Workout Plan:** Include specific exercises, sets, and repetitions. Tailor the plan based on the individual's fitness goal.\n\n\
2. **Diet Plan:** Suggest a daily meal plan with details on the type and quantity of food. Consider nutritional requirements based on the fitness goal.\n\n\
Provide a detailed and actionable plan for the user."

    response = openai.Completion.create(
        engine="text-davinci-002",  # You can experiment with different engines
        prompt=prompt,
        max_tokens=2000,  # Adjust based on desired response length
        temperature=0.7,  # Adjust for randomness (higher values for more randomness)
        stop=None  # You can customize stop criteria for the response
    )
    return response.choices[0].text.strip()

# Streamlit web app
def main():
    st.title("Fitness Planner")

    # User input for height, weight, and fitness goal
    height = st.slider("Select your height (in cm):", 100, 250, 170)
    weight = st.slider("Select your weight (in kg):", 30, 200, 70)
    fitness_goal = st.radio("Select your fitness goal:", ["Weight Loss", "Muscle Gain", "Maintain Fitness"])

    # Button to trigger the fitness plan generation
    if st.button("Get Your Plan"):
        # Call the GPT-3 function
        fitness_plan = generate_fitness_plan(height, weight, fitness_goal)

        # Display the generated plan
        st.subheader("Your Personalized Fitness Plan:")
        st.write(fitness_plan)

# Run the Streamlit app
if __name__ == "__main__":
    main()
