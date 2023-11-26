import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Define functions for loading Lottie animations and local CSS
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations
lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_FYx0Ph.json")
music = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ikk4jhps.json")
podcast = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_JjpNLdaKYX.json")

# Load images
img_contact_form = Image.open("home.jpg")
img_lottie_animation = Image.open("home.jpg")

# Set page configuration
st.set_page_config(page_title="Fitness Trainer", page_icon=":tada:", layout="wide")

# Sidebar navigation with hyperlinks
page_links = {
    "main": "main",
    "Tutorials": "Tutorials",
    "Train": "Train",
    "Chatbot": "Chatbot",
    "Nutrition": "Nutrition",
    "diet": "diet"
}

# Apply custom CSS styles
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
        color: #333;
    }
    .sidebar .css-ewapu8 {
        background-color: #4285f4;
        color: white;
    }
    .sidebar .css-ewapu8:hover {
        background-color: #1656a3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

selected_page = st.sidebar.radio("Select a page", list(page_links.keys()))

if selected_page == "main":
    st.title("Home page")

    # Main content
    with st.container():
        st.subheader("Hello, welcome to our website :wave:")
        st.title("AI Fitness Trainer")
        st.write("Step into a fitter future: Welcome to your fitness revolution!")

    # About us section
    with st.container():
        st.write("---")
        st.write("## About us :point_down:")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("")
            st.write(
                """
                - We are thrilled to have you here on our platform dedicated to empowering and inspiring individuals on their journey towards a healthier and fitter lifestyle. Whether you're a seasoned fitness enthusiast or just starting your fitness journey, we have everything you need to reach your goals and achieve the best version of yourself.

                - What sets us apart is the fact that we provide personalized assistance at the comfort of your home or any place of your choice at a price that is both convenient and much cheaper than traditional gyms.

                Let your fitness journey start here!
                Join us today and embark on a transformative experience that will enhance your physical and mental well-being. Let's build strength, resilience, and a healthier future together!
                """
            )

        with right_column:
            st_lottie(lottie_hello, height=300, key="hello")

    # Projects section
    with st.container():
        st.write("---")
        st.header("Get fit, Jam on, Repeat :headphones:")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st_lottie(music, height=300, key="music")
        with text_column:
            st.write("##")
            st.subheader("Workout music")
            st.write(
                """
                Power up your workout with the ultimate music fuel!
                """
            )
            st.markdown("[Have a Listen...](https://open.spotify.com/playlist/6N0Vl77EzPm13GIOlEkoJn?si=9207b7744d094bd3)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st_lottie(podcast, height=300, key="podcast")
        with text_column:
            st.write("##")
            st.subheader("Podcast")
            st.write(
                """
                Take your workouts to the next level with our immersive podcast that pumps you up from start to finish!
                """
            )
            st.markdown("[Have a listen...](https://open.spotify.com/playlist/09Ig7KfohF5WmU9RhbDBjs?si=jyZ79y3wQgezrEDHim0NvQ)")

    # Contact section
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Contact form
        contact_form = """
        <form action="https://formsubmit.co/c722428e42528bf09a0c149f6b7d3909" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit" style="background-color: #4285f4; color: white;">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

# Display content for the selected page
elif selected_page == "Tutorials":
    st.title("Tutorials")
    import streamlit as st
    import json

    import requests
    import streamlit as st
    from streamlit_lottie import st_lottie
    from PIL import Image

    # Lottie Files: https://lottiefiles.com/

    html = """
       <div style="background-color:#025246 ;padding:10px">
       <h2 style="color:white;text-align:center;">Tutorial</h2>
       </div>"""
    st.markdown(html, unsafe_allow_html=True)

    # New
    img1 = Image.open("dumbbell.webp")
    img2 = Image.open("squats.jpg")
    img3 = Image.open("pushups.jpeg")
    img4 = Image.open("shoulder.jpeg")

    app_mode = st.sidebar.selectbox("Choose the tutorial",
                                    ["About", "Bicep Curls", "Squats", "Pushups", "Shoulder press"])
    if app_mode == "About":
        # st_lottie(lottie_hello,key="hello")

        with st.container():
            st.write("---")
            st.header("Have a look at these video tutorials")
            st.write("##")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(img1, width=325)
            with text_column:
                st.subheader("Bicep Curls")
                st.write(
                    """
                    Get armed with knowledge! Watch this bicep curl tutorial and unlock the secret to sleeve-busting strength!
                    """
                )
                st.markdown("[Watch Video...](https://youtu.be/ykJmrZ5v0Oo)")

        with st.container():
            image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img2, width=325)
        with text_column:
            st.subheader("Squats")
            st.write(
                """
                Get lower, get stronger! Dive into this squat tutorial and unlock the power of a rock-solid foundation!.
                """
            )
            st.markdown("[Watch Video...](https://youtu.be/YaXPRqUwItQ)")

        with st.container():
            image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img3, width=325)
        with text_column:
            st.subheader("Pushups")
            st.write(
                """
                Push your limits, pump up your power! Join us for this push-up tutorial and unleash your inner strength!.
                """
            )
            st.markdown("[Watch Video...](https://youtu.be/IODxDxX7oi4)")

        with st.container():
            image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img4, width=325)
        with text_column:
            st.subheader("Shoulder press")
            st.write(
                """
                Elevate your strength, shoulder to shoulder! Don't miss this shoulder press tutorial to reach new heights of power!.
                """
            )
            st.markdown("[Watch Video...](https://youtu.be/qEwKCR5JCog)")


    elif app_mode == "Bicep Curls":
        st.markdown("## Bicep Curls")
        st.markdown("Here's a step-by-step tutorial for bicep curls:")

        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.write("""
               - Stand up straight with a dumbbell in each hand. Keep your elbows close to your torso and rotate the palms of your hands until they are facing forward. This will be your starting position.

               - Now, keeping the upper arms stationary, exhale and curl the weights while contracting your biceps. 

               - Continue to raise the weights until your biceps are fully contracted and the dumbbells are at shoulder level. 

               - Hold the contracted position for a brief pause as you squeeze your biceps.

               - Then, inhale and slowly begin to lower the dumbbells back to the starting position.

               Remember, it's important to use appropriate weight for your fitness level and gradually increase the resistance as you get stronger.    
               """)
        with col2:
            st.image("bicep.gif")



    elif app_mode == "Squats":
        st.markdown("## Squats")
        st.markdown("Here's a step-by-step tutorial for performing Squats:")

        col1, col2 = st.columns(2)
        st.write("##")
        with col1:
            st.write("""
               - Stand with your feet slightly wider than shoulder-width apart, toes pointing slightly outward. You can also experiment with different foot positions to find what's most comfortable for you.

               - Engage your core muscles by pulling your belly button in towards your spine. Keep your back straight and maintain good posture throughout the exercise.

               - Begin the squat by bending your knees and pushing your hips back, as if you're sitting back into a chair. Make sure to keep your weight on your heels and your knees tracking in line with your toes.

               - Lower your body down until your thighs are parallel to the ground. If you have the flexibility and mobility, you can go lower, but it's important to maintain proper form throughout the movement.

               - Pause for a moment at the bottom of the squat, and then begin to push through your heels and straighten your legs to return to the starting position. Keep your core engaged and maintain control of the movement.

               - As you come back up, avoid locking your knees at the top. Maintain a slight bend in your knees to keep tension on the muscles and avoid unnecessary strain.

               - Repeat the squat for your desired number of repetitions. Start with a weight or bodyweight that allows you to maintain proper form, and gradually increase the difficulty as you become more comfortable and stronger.

               Additional tips:
               - Keep your chest up and your gaze forward throughout the exercise. Avoid rounding your back or looking down.
               - Exhale as you push up from the squat and inhale as you lower down. Breathing properly helps stabilize your core and maintain control.

               Remember, it's important to listen to your body and start with a weight or intensity level that is appropriate for your fitness level. Gradually progress as you gain strength and confidence in your squatting technique.   
               """)
        with col2:
            st.image("squats.gif")

    elif app_mode == "Pushups":
        st.markdown("## Pushups")
        st.markdown("Here's a step-by-step tutorial for performing Pushups:")

        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.write("""
               - Start in a high plank position with your palms flat on the floor, hands shoulder-width apart, shoulders stacked directly above your wrists, legs extended behind you, and your core and glutes engaged.

               - Bend your elbows and begin to lower your body down to the floor. When your chest grazes it, extend your elbows and return to the start. Focus on keeping your elbows close to your body during the movement.

               - Complete as many reps as you can with good form. If you can't perform at least 3–5 reps, modify the movement by dropping to your knees or doing wall push-ups.

               Remember, it's important to listen to your body and start with a weight or intensity level that is appropriate for your fitness level. Gradually progress as you gain strength and confidence in your pushup technique.

               """)
        with col2:
            st.image("pushups.gif")

    elif app_mode == "Shoulder press":
        st.markdown("## Shoulder press")
        st.markdown("Here's a step-by-step tutorial for performing Shoulder Press:")

        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.write("""
               - Stand with your feet shoulder-width apart and hold a dumbbell in each hand. Raise the dumbbells to your shoulders, palms facing forward. This is your starting position.

               - Press the weights upward until your arms are fully extended overhead. Keep your head and neck stationary.

               - Pause at the top, then lower the weights back to the starting position.

               Remember, it's important to listen to your body and start with a weight or intensity level that is appropriate for your fitness level. Gradually progress as you gain strength and confidence in your shoulder press technique.

               """)
        with col2:
            st.image("shoulder.gif")
elif selected_page == "Train":
    st.title("Train")
    import streamlit as st
    import json

    import requests

    import cv2
    from cvzone.PoseModule import PoseDetector
    import math
    import numpy as np
    import plotly.graph_objects as go
    import tempfile

    # Lottie Files: https://lottiefiles.com/

    html = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Train here</h2>
    </div>"""
    st.markdown(html, unsafe_allow_html=True)

    app_mode = st.sidebar.selectbox("Choose the exercise",
                                    ["About", "Left Dumbbell", "Right Dumbbell", "Squats", "Pushups", "Shoulder press"])
    if app_mode == "About":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("## Welcome to the Training arena")
            st.markdown("Choose the workout you wish to do from the sidebar")
            st.write("##")
            st.write("""
            Here are few general instructions to follow while doing the workout:

            - It is necessary for you to provide web cam access. If you do not have a webcam, kindly attach an external camera while performing exercises.
            - Please avoid crowded places as the model can only detect 1 person. 
            - Please ensure that the surrounding is well lit so that the camera can detect you.
            - Please make sure the camera is focused on you based on the exercise so that the system can detect the angles and give you the correct input on form and count reps.

            With all that out of the way, Its time for you to get pumped up
            """)

        with col2:
            img = st.image('ham.gif')



    elif app_mode == "Left Dumbbell":
        st.markdown("## Left Dumbbell")
        weight1 = st.slider('What is your weight?', 20, 130, 40)
        st.write("I'm ", weight1, 'kgs')

        st.write("-------------")

        goal_calorie1 = st.slider('Set a goal calorie to burn', 10, 200, 15)
        st.write("I want to burn", goal_calorie1, 'kcal')

        st.write("-------------")

        st.write(" Click on the Start button to start the live video feed.")
        st.write("##")


        class angleFinder:
            def __init__(self, lmlist, p1, p2, p3, drawPoints):
                self.lmlist = lmlist
                self.p1 = p1
                self.p2 = p2
                self.p3 = p3

                self.drawPoints = drawPoints

            #    finding angles

            def angle(self):
                if len(self.lmlist) != 0:
                    point1 = self.lmlist[self.p1]
                    point2 = self.lmlist[self.p2]
                    point3 = self.lmlist[self.p3]

                    x1, y1 = point1[1:-1]
                    x2, y2 = point2[1:-1]
                    x3, y3 = point3[1:-1]

                    # calculating angle for left arm
                    leftHandAngle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                                 math.atan2(y1 - y2, x1 - x2))

                    leftHandAngle = int(np.interp(leftHandAngle, [42, 143], [100, 0]))

                    # drawing circles and lines on selected points
                    if self.drawPoints == True:
                        cv2.circle(img, (x1, y1), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x1, y1), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x2, y2), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x2, y2), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x3, y3), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x3, y3), 15, (0, 255, 0), 6)

                        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
                        cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 4)

                    return leftHandAngle


        if 'type' not in st.session_state:
            st.session_state.type = None


        def handle_click_start():
            st.session_state.type = "Start"


        def handle_click_stop():
            st.write(st.session_state.counter1)
            st.session_state.type = "Stop"


        start_button = st.button('Start', on_click=handle_click_start)
        stop_button = st.button('Stop', on_click=handle_click_stop)

        # defining some variables
        counter = 0
        direction = 0

        frame_placeholder = st.empty()

        detector = PoseDetector(detectionCon=0.7, trackCon=0.7)

        if st.session_state['type'] == 'Start':

            cap = cv2.VideoCapture(0)
            while cap.isOpened():
                ret, img = cap.read()
                img = cv2.resize(img, (640, 480))

                detector.findPose(img, draw=0)
                lmList, bboxInfo = detector.findPosition(img, bboxWithHands=0, draw=False)

                angle1 = angleFinder(lmList, 11, 13, 15, drawPoints=True)
                left = angle1.angle()

                if left == None:
                    left = 0

                # Counting number of shoulder ups
                if left >= 90:
                    if direction == 0:
                        counter += 0.5
                        st.session_state.counter1 = counter
                        direction = 1
                if left <= 70:
                    if direction == 1:
                        counter += 0.5
                        st.session_state.counter1 = counter
                        direction = 0

                # putting scores on the screen
                cv2.rectangle(img, (0, 0), (120, 120), (255, 0, 0), -1)
                cv2.putText(img, str(int(counter)), (1, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (0, 0, 255), 6)

                # Converting values for rectangles
                leftval = np.interp(left, [0, 100], [480, 280])

                # Drawing left rectangle and putting text
                cv2.rectangle(img, (582, 280), (632, 480), (0, 0, 255), 5)
                cv2.rectangle(img, (582, int(leftval)), (632, 480), (0, 0, 255), -1)

                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                frame_placeholder.image(img, "RGB")


        elif st.session_state['type'] == 'Stop':
            st.write("The video capture has ended")

            st.write("---------")
            st.write("## Anaytics")
            st.write("You did ", st.session_state.counter1, " reps")

            calories1 = 3.8 * weight1 / st.session_state.counter1
            if calories1 < goal_calorie1:
                st.write("You have burned ", calories1, "kcal of calories")
                st.write("You have not achieved your goal. Try again")

            else:
                st.write("You have burned ", calories1, "kcal of calories")
                st.write("You have achieved your goal. Congratulations")

            fig = go.Figure(data=[go.Bar(x=['Bicep Curls'], y=[calories1], name='Calories Burned')])

            fig.add_trace(go.Bar(x=['Bicep Curls'], y=[goal_calorie1], name='Goal Calorie'))

            # Set chart layout
            fig.update_layout(
                title='Calories Burned for Bicep Curls',
                xaxis_title='Exercise',
                yaxis_title='Calories Burned'
            )

            # Display the chart using Streamlit
            st.plotly_chart(fig)








    elif app_mode == "Right Dumbbell":
        st.markdown("## Right Dumbbell")
        weight2 = st.slider('What is your weight?', 20, 130, 40)
        st.write("I'm ", weight2, 'kgs')

        st.write("-------------")

        goal_calorie2 = st.slider('Set a goal calorie to burn', 10, 200, 15)
        st.write("I want to burn", goal_calorie2, 'kcal')

        st.write("-------------")

        st.write(" Click on the Start button to start the live video feed.")
        st.write("##")


        # Creating Angle finder class
        class angleFinder:
            def __init__(self, lmlist, p1, p2, p3, drawPoints):
                self.lmlist = lmlist
                self.p1 = p1
                self.p2 = p2
                self.p3 = p3

                self.drawPoints = drawPoints

            #    finding angles

            def angle(self):
                if len(self.lmlist) != 0:
                    point1 = self.lmlist[self.p1]
                    point2 = self.lmlist[self.p2]
                    point3 = self.lmlist[self.p3]

                    x1, y1 = point1[1:-1]
                    x2, y2 = point2[1:-1]
                    x3, y3 = point3[1:-1]

                    # calculating angle for left arm
                    leftHandAngle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                                 math.atan2(y1 - y2, x1 - x2))

                    leftHandAngle = int(np.interp(leftHandAngle, [42, 143], [100, 0]))

                    # drawing circles and lines on selected points
                    if self.drawPoints == True:
                        cv2.circle(img, (x1, y1), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x1, y1), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x2, y2), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x2, y2), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x3, y3), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x3, y3), 15, (0, 255, 0), 6)

                        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
                        cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 4)

                    return leftHandAngle


        if 'type' not in st.session_state:
            st.session_state.type = None


        def handle_click_start():
            st.session_state.type = "Start2"


        def handle_click_stop():
            st.write(st.session_state.counter2)
            st.session_state.type = "Stop2"


        start_button = st.button('Start', on_click=handle_click_start)
        stop_button = st.button('Stop', on_click=handle_click_stop)

        # defining some variables
        counter = 0
        direction = 0

        frame_placeholder = st.empty()

        detector = PoseDetector(detectionCon=0.7, trackCon=0.7)

        if st.session_state['type'] == 'Start2':
            cap = cv2.VideoCapture(0)
            while cap.isOpened():
                ret, img = cap.read()
                img = cv2.resize(img, (640, 480))

                detector.findPose(img, draw=0)
                lmList, bboxInfo = detector.findPosition(img, bboxWithHands=0, draw=False)

                angle1 = angleFinder(lmList, 12, 14, 16, drawPoints=True)
                left = angle1.angle()

                if left == None:
                    left = 0

                # Counting number of shoulder ups
                if left >= 90:
                    if direction == 0:
                        counter += 0.5
                        st.session_state.counter2 = counter
                        direction = 1
                if left <= 70:
                    if direction == 1:
                        counter += 0.5
                        st.session_state.counter2 = counter
                        direction = 0

                # putting scores on the screen
                cv2.rectangle(img, (0, 0), (120, 120), (255, 0, 0), -1)
                cv2.putText(img, str(int(counter)), (1, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (0, 0, 255), 6)

                # Converting values for rectangles
                leftval = np.interp(left, [0, 100], [480, 280])

                # Drawing left rectangle and putting text
                cv2.rectangle(img, (582, 280), (632, 480), (0, 0, 255), 5)
                cv2.rectangle(img, (582, int(leftval)), (632, 480), (0, 0, 255), -1)

                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                frame_placeholder.image(img, "RGB")

                cv2.waitKey(1)

        elif st.session_state['type'] == 'Stop2':
            st.write("The video capture has ended")

            st.write("---------")
            st.write("## Anaytics")
            st.write("You did ", st.session_state.counter2, " reps")

            calories2 = 3.8 * weight2 / st.session_state.counter2
            if calories2 < goal_calorie2:
                st.write("You have burned ", calories2, "kcal of calories")
                st.write("You have not achieved your goal. Try again")

            else:
                st.write("You have burned ", calories2, "kcal of calories")
                st.write("You have achieved your goal. Congratulations")

            fig = go.Figure(data=[go.Bar(x=['Bicep Curls'], y=[calories2], name='Calories Burned')])

            fig.add_trace(go.Bar(x=['Bicep Curls'], y=[goal_calorie2], name='Goal Calorie'))

            # Set chart layout
            fig.update_layout(
                title='Calories Burned for Bicep Curls',
                xaxis_title='Exercise',
                yaxis_title='Calories Burned'
            )

            # Display the chart using Streamlit
            st.plotly_chart(fig)


    elif app_mode == "Squats":
        st.markdown("## Squats")
        weight3 = st.slider('What is your weight?', 20, 130, 40)
        st.write("I'm ", weight3, 'kgs')

        st.write("-------------")

        goal_calorie3 = st.slider('Set a goal calorie to burn', 10, 200, 15)
        st.write("I want to burn", goal_calorie3, 'kcal')

        st.write("-------------")

        st.write(" Click on the Start button to start the live video feed.")
        st.write("##")


        # Creating Angle finder class
        class angleFinder:
            def __init__(self, lmlist, p1, p2, p3, p4, p5, p6, drawPoints):
                self.lmlist = lmlist
                self.p1 = p1
                self.p2 = p2
                self.p3 = p3
                self.p4 = p4
                self.p5 = p5
                self.p6 = p6
                self.drawPoints = drawPoints

            #    finding angles

            def angle(self):
                if len(self.lmlist) != 0:
                    point1 = self.lmlist[self.p1]
                    point2 = self.lmlist[self.p2]
                    point3 = self.lmlist[self.p3]
                    point4 = self.lmlist[self.p4]
                    point5 = self.lmlist[self.p5]
                    point6 = self.lmlist[self.p6]

                    x1, y1 = point1[1:-1]
                    x2, y2 = point2[1:-1]
                    x3, y3 = point3[1:-1]
                    x4, y4 = point4[1:-1]
                    x5, y5 = point5[1:-1]
                    x6, y6 = point6[1:-1]

                    # calculating angle for left leg
                    leftLegAngle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                                math.atan2(y1 - y2, x1 - x2))

                    leftLegAngle = int(np.interp(leftLegAngle, [42, 143], [100, 0]))

                    # drawing circles and lines on selected points
                    if self.drawPoints == True:
                        cv2.circle(img, (x1, y1), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x1, y1), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x2, y2), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x2, y2), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x3, y3), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x3, y3), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x4, y4), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x4, y4), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x5, y5), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x5, y5), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x6, y6), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x6, y6), 15, (0, 255, 0), 6)

                        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
                        cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 4)
                        cv2.line(img, (x4, y4), (x5, y5), (0, 0, 255), 4)
                        cv2.line(img, (x5, y5), (x6, y6), (0, 0, 255), 4)
                        cv2.line(img, (x1, y1), (x4, y4), (0, 0, 255), 4)

                    return leftLegAngle


        if 'type' not in st.session_state:
            st.session_state.type = None


        def handle_click_start():
            st.session_state.type = "Start3"


        def handle_click_stop():
            st.write(st.session_state.counter3)
            st.session_state.type = "Stop3"


        start_button = st.button('Start', on_click=handle_click_start)
        stop_button = st.button('Stop', on_click=handle_click_stop)

        # defining some variables
        counter = 0
        direction = 0

        frame_placeholder = st.empty()

        detector = PoseDetector(detectionCon=0.7, trackCon=0.7)

        if st.session_state['type'] == 'Start3':
            cap = cv2.VideoCapture(0)
            while cap.isOpened():
                ret, img = cap.read()
                img = cv2.resize(img, (640, 480))

                detector.findPose(img, draw=0)
                lmList, bboxInfo = detector.findPosition(img, bboxWithHands=0, draw=False)

                angle1 = angleFinder(lmList, 24, 26, 28, 23, 25, 27, drawPoints=True)
                left = angle1.angle()

                if left == None:
                    left = 0

                # Counting number of shoulder ups
                if left >= 90:
                    if direction == 0:
                        counter += 0.5
                        st.session_state.counter3 = counter
                        direction = 1
                if left <= 70:
                    if direction == 1:
                        counter += 0.5
                        st.session_state.counter3 = counter
                        direction = 0

                # putting scores on the screen
                cv2.rectangle(img, (0, 0), (120, 120), (255, 0, 0), -1)
                cv2.putText(img, str(int(counter)), (1, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (0, 0, 255), 6)

                # Converting values for rectangles
                leftval = np.interp(left, [0, 100], [480, 280])

                # Drawing left rectangle and putting text
                cv2.rectangle(img, (582, 280), (632, 480), (0, 0, 255), 5)
                cv2.rectangle(img, (582, int(leftval)), (632, 480), (0, 0, 255), -1)

                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                frame_placeholder.image(img, "RGB")

                cv2.waitKey(1)

        elif st.session_state['type'] == 'Stop3':
            st.write("The video capture has ended")

            st.write("---------")
            st.write("## Anaytics")
            st.write("You did ", st.session_state.counter3, " reps")

            calories3 = 6.0 * weight3 / st.session_state.counter3
            if calories3 < goal_calorie3:
                st.write("You have burned ", calories3, "kcal of calories")
                st.write("You have not achieved your goal. Try again")

            else:
                st.write("You have burned ", calories3, "kcal of calories")
                st.write("You have achieved your goal. Congratulations")

            fig = go.Figure(data=[go.Bar(x=['Bicep Curls'], y=[calories3], name='Calories Burned')])

            fig.add_trace(go.Bar(x=['Bicep Curls'], y=[goal_calorie3], name='Goal Calorie'))

            # Set chart layout
            fig.update_layout(
                title='Calories Burned for Bicep Curls',
                xaxis_title='Exercise',
                yaxis_title='Calories Burned'
            )

            # Display the chart using Streamlit
            st.plotly_chart(fig)



    elif app_mode == "Pushups":
        st.markdown("## Pushups")
        weight4 = st.slider('What is your weight?', 20, 130, 40)
        st.write("I'm ", weight4, 'kgs')

        st.write("-------------")

        goal_calorie4 = st.slider('Set a goal calorie to burn', 10, 200, 15)
        st.write("I want to burn", goal_calorie4, 'kcal')

        st.write("-------------")

        st.write(" Click on the Start button to start the live video feed.")
        st.write("##")


        # cap = cv2.VideoCapture('vid1.mp4')

        def angles(lmlist, p1, p2, p3, p4, p5, p6, drawpoints):
            global counter
            global direction

            if len(lmlist) != 0:
                point1 = lmlist[p1]
                point2 = lmlist[p2]
                point3 = lmlist[p3]
                point4 = lmlist[p4]
                point5 = lmlist[p5]
                point6 = lmlist[p6]

                x1, y1 = point1[1:-1]
                x2, y2 = point2[1:-1]
                x3, y3 = point3[1:-1]
                x4, y4 = point4[1:-1]
                x5, y5 = point5[1:-1]
                x6, y6 = point6[1:-1]

                if drawpoints == True:
                    cv2.circle(img, (x1, y1), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x1, y1), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x2, y2), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x2, y2), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x3, y3), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x3, y3), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x4, y4), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x4, y4), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x5, y5), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x5, y5), 15, (0, 255, 0), 5)
                    cv2.circle(img, (x6, y6), 10, (255, 0, 255), 5)
                    cv2.circle(img, (x6, y6), 15, (0, 255, 0), 5)

                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)
                    cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 6)
                    cv2.line(img, (x4, y4), (x5, y5), (0, 0, 255), 6)
                    cv2.line(img, (x5, y5), (x6, y6), (0, 0, 255), 6)
                    cv2.line(img, (x1, y1), (x4, y4), (0, 0, 255), 6)

                lefthandangle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                             math.atan2(y1 - y2, x1 - x2))

                righthandangle = math.degrees(math.atan2(y6 - y5, x6 - x5) -
                                              math.atan2(y4 - y5, x4 - x5))

                # print(lefthandangle,righthandangle)

                leftHandAngle = int(np.interp(lefthandangle, [-30, 180], [100, 0]))
                rightHandAngle = int(np.interp(righthandangle, [34, 173], [100, 0]))

                left, right = leftHandAngle, rightHandAngle

                if left >= 60 and right >= 60:
                    if direction == 0:
                        counter += 0.5
                        st.session_state.counter4 = counter
                        direction = 1
                if left <= 60 and right <= 60:
                    if direction == 1:
                        counter += 0.5
                        st.session_state.counter4 = counter
                        direction = 0

                cv2.rectangle(img, (0, 0), (120, 120), (255, 0, 0), -1)
                cv2.putText(img, str(int(counter)), (20, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (0, 0, 255), 7)

                leftval = np.interp(right, [0, 100], [400, 200])
                rightval = np.interp(right, [0, 100], [400, 200])

                cv2.putText(img, 'R', (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
                cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
                cv2.rectangle(img, (8, int(rightval)), (50, 400), (255, 0, 0), -1)

                cv2.putText(img, 'L', (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
                cv2.rectangle(img, (952, 200), (995, 400), (0, 255, 0), 5)
                cv2.rectangle(img, (952, int(leftval)), (995, 400), (255, 0, 0), -1)

                if left > 70:
                    cv2.rectangle(img, (952, int(leftval)), (995, 400), (0, 0, 255), -1)

                if right > 70:
                    cv2.rectangle(img, (8, int(leftval)), (50, 400), (0, 0, 255), -1)


        if 'type' not in st.session_state:
            st.session_state.type = None


        def handle_click_start():
            st.session_state.type = "Start4"


        def handle_click_stop():
            st.write(st.session_state.counter4)
            st.session_state.type = "Stop4"


        start_button = st.button('Start', on_click=handle_click_start)
        stop_button = st.button('Stop', on_click=handle_click_stop)

        counter = 0
        direction = 0

        frame_placeholder = st.empty()

        pd = PoseDetector(detectionCon=0.7, trackCon=0.7)

        if st.session_state['type'] == 'Start4':
            cap = cv2.VideoCapture(0)
            while cap.isOpened():
                ret, img = cap.read()
                # if not ret:
                #     cap = cv2.VideoCapture('vid1.mp4')
                #     continue

                img = cv2.resize(img, (1000, 500))
                # cvzone.putTextRect(img,'AI Push Up Counter',[345,30],thickness=2,border=2,scale=2.5)
                pd.findPose(img, draw=0)
                lmlist, bbox = pd.findPosition(img, draw=0, bboxWithHands=0)

                angles(lmlist, 11, 13, 15, 12, 14, 16, drawpoints=1)

                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                frame_placeholder.image(img, "RGB")

                cv2.waitKey(1)

        elif st.session_state['type'] == 'Stop4':
            st.write("The video capture has ended")

            st.write("---------")
            st.write("## Anaytics")
            st.write("You did ", st.session_state.counter4, " reps")

            calories4 = 8.0 * weight4 / st.session_state.counter4
            if calories4 < goal_calorie4:
                st.write("You have burned ", calories4, "kcal of calories")
                st.write("You have not achieved your goal. Try again")

            else:
                st.write("You have burned ", calories4, "kcal of calories")
                st.write("You have achieved your goal. Congratulations")

            fig = go.Figure(data=[go.Bar(x=['Bicep Curls'], y=[calories4], name='Calories Burned')])

            fig.add_trace(go.Bar(x=['Bicep Curls'], y=[goal_calorie4], name='Goal Calorie'))

            # Set chart layout
            fig.update_layout(
                title='Calories Burned for Bicep Curls',
                xaxis_title='Exercise',
                yaxis_title='Calories Burned'
            )

            # Display the chart using Streamlit
            st.plotly_chart(fig)


    elif app_mode == "Shoulder press":
        st.markdown("## Shoulder Press")
        weight5 = st.slider('What is your weight?', 20, 130, 40)
        st.write("I'm ", weight5, 'kgs')

        st.write("-------------")

        goal_calorie5 = st.slider('Set a goal calorie to burn', 10, 200, 15)
        st.write("I want to burn", goal_calorie5, 'kcal')

        st.write("-------------")

        st.write(" Click on the Start button to start the live video feed.")
        st.write("##")


        # Creating Angle finder class
        class angleFinder:
            def __init__(self, lmlist, p1, p2, p3, p4, p5, p6, drawPoints):
                self.lmlist = lmlist
                self.p1 = p1
                self.p2 = p2
                self.p3 = p3
                self.p4 = p4
                self.p5 = p5
                self.p6 = p6
                self.drawPoints = drawPoints

            #    finding angles

            def angle(self):
                if len(self.lmlist) != 0:
                    point1 = self.lmlist[self.p1]
                    point2 = self.lmlist[self.p2]
                    point3 = self.lmlist[self.p3]
                    point4 = self.lmlist[self.p4]
                    point5 = self.lmlist[self.p5]
                    point6 = self.lmlist[self.p6]

                    x1, y1 = point1[1:-1]
                    x2, y2 = point2[1:-1]
                    x3, y3 = point3[1:-1]
                    x4, y4 = point4[1:-1]
                    x5, y5 = point5[1:-1]
                    x6, y6 = point6[1:-1]

                    # calculating angle for left and right hands
                    leftHandAngle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                                 math.atan2(y1 - y2, x1 - x2))

                    rightHandAngle = math.degrees(math.atan2(y6 - y5, x6 - x5) -
                                                  math.atan2(y4 - y5, x4 - x5))

                    leftHandAngle = int(np.interp(leftHandAngle, [-170, 180], [100, 0]))
                    # rightHandAngle = int(np.interp(rightHandAngle, [-50, 20], [100, 0]))
                    rightHandAngle = int(np.interp(rightHandAngle, [-170, 180], [100, 0]))

                    # drawing circles and lines on selected points
                    if self.drawPoints == True:
                        cv2.circle(img, (x1, y1), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x1, y1), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x2, y2), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x2, y2), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x3, y3), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x3, y3), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x4, y4), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x4, y4), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x5, y5), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x5, y5), 15, (0, 255, 0), 6)
                        cv2.circle(img, (x6, y6), 10, (0, 255, 255), 5)
                        cv2.circle(img, (x6, y6), 15, (0, 255, 0), 6)

                        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
                        cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 4)
                        cv2.line(img, (x4, y4), (x5, y5), (0, 0, 255), 4)
                        cv2.line(img, (x5, y5), (x6, y6), (0, 0, 255), 4)
                        cv2.line(img, (x1, y1), (x4, y4), (0, 0, 255), 4)

                    return list([leftHandAngle, rightHandAngle])


        if 'type' not in st.session_state:
            st.session_state.type = None


        def handle_click_start():
            st.session_state.type = "Start5"


        def handle_click_stop():
            st.write(st.session_state.counter5)
            st.session_state.type = "Stop5"


        start_button = st.button('Start', on_click=handle_click_start)
        stop_button = st.button('Stop', on_click=handle_click_stop)

        # defining some variables
        counter = 0
        direction = 0

        frame_placeholder = st.empty()

        detector = PoseDetector(detectionCon=0.7, trackCon=0.7)

        if st.session_state['type'] == 'Start5':
            cap = cv2.VideoCapture(0)

            while cap.isOpened():
                ret, img = cap.read()
                img = cv2.resize(img, (1000, 600))

                detector.findPose(img, draw=0)
                lmList, bboxInfo = detector.findPosition(img, bboxWithHands=0, draw=False)

                angle1 = angleFinder(lmList, 11, 13, 15, 12, 14, 16, drawPoints=True)
                hands = angle1.angle()

                if hands == None:
                    continue

                left, right = hands[0:]

                # Counting number of shoulder ups
                if left >= 90 and right >= 90:
                    if direction == 0:
                        counter += 0.5
                        st.session_state.counter5 = counter
                        direction = 1
                if left <= 70 and right <= 70:
                    if direction == 1:
                        counter += 0.5
                        st.session_state.counter5 = counter
                        direction = 0

                # putting scores on the screen
                cv2.rectangle(img, (0, 0), (120, 120), (255, 0, 0), -1)
                cv2.putText(img, str(int(counter)), (1, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (0, 0, 255), 6)

                # Converting values for rectangles
                leftval = np.interp(left, [0, 100], [400, 200])
                rightval = np.interp(right, [0, 100], [400, 200])

                # For color changing
                value_left = np.interp(left, [0, 100], [0, 100])
                value_right = np.interp(right, [0, 100], [0, 100])

                # Drawing right rectangle and putting text
                cv2.putText(img, 'R', (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 5)
                cv2.rectangle(img, (8, 200), (50, 400), (0, 255, 0), 5)
                cv2.rectangle(img, (8, int(rightval)), (50, 400), (255, 0, 0), -1)

                # Drawing left rectangle and putting text
                cv2.putText(img, 'L', (900, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 5)
                cv2.rectangle(img, (882, 200), (932, 400), (0, 255, 0), 5)
                cv2.rectangle(img, (882, int(leftval)), (932, 400), (255, 0, 0), -1)

                if value_left > 70:
                    cv2.rectangle(img, (882, int(leftval)), (932, 400), (0, 0, 255), -1)

                if value_right > 70:
                    cv2.rectangle(img, (8, int(rightval)), (50, 400), (0, 0, 255), -1)

                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                frame_placeholder.image(img, "RGB")

                cv2.waitKey(1)

        elif st.session_state['type'] == 'Stop5':
            st.write("The video capture has ended")

            st.write("---------")
            st.write("## Anaytics")
            st.write("You did ", st.session_state.counter5, " reps")

            calories5 = 5.5 * weight5 / st.session_state.counter5
            if calories5 < goal_calorie5:
                st.write("You have burned ", calories5, "kcal of calories")
                st.write("You have not achieved your goal. Try again")

            else:
                st.write("You have burned ", calories5, "kcal of calories")
                st.write("You have achieved your goal. Congratulations")

            fig = go.Figure(data=[go.Bar(x=['Bicep Curls'], y=[calories5], name='Calories Burned')])

            fig.add_trace(go.Bar(x=['Bicep Curls'], y=[goal_calorie5], name='Goal Calorie'))

            # Set chart layout
            fig.update_layout(
                title='Calories Burned for Bicep Curls',
                xaxis_title='Exercise',
                yaxis_title='Calories Burned'
            )

            # Display the chart using Streamlit
            st.plotly_chart(fig)

elif selected_page == "Chatbot":
    st.title("Chatbot")
    import openai
    import toml
    import streamlit as st


    def show_messages(text):
        messages_str = [
            f"<span style='color: green;'><b>USER</b>: {_['content']}</span></br>" if _[
                                                                                          'role'] == 'user' else f"<span style='color: white;'><b>SYSTEM</b>: {_['content']}</span></br></br>"
            for _ in st.session_state["messages"][1:]
        ]
        text.markdown("Messages", unsafe_allow_html=True)
        text.markdown(str("\n".join(messages_str)), unsafe_allow_html=True)


    openai.api_key = "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"

    BASE_PROMPT = [{"role": "system", 'content': """
    You are Donnie, an automated Gym assistant to provide workout routines for the users and give suggestions. \
    You first greet the customer, then ask them what type of workout routine they want, \
    give them a few workout options and wait for them to finalize\ if they ask for changes make those changes accordingly\
    , then summarize it and check for a final \
    time if the user wants to add anything else. \
    If it's a split, you ask for an upper body lower body or back chest and legs split. \

    Make sure to clarify all questions about exercises and form \
    also make sure to talk only about fitness and fitness related topics\
    You respond in a short, very conversational friendly style. \



    """}]

    if "messages" not in st.session_state:
        st.session_state["messages"] = BASE_PROMPT

    st.header("FIT-BOT")

    text = st.empty()
    show_messages(text)

    if 'something' not in st.session_state:
        st.session_state.something = ''


    def submit():
        st.session_state.something = st.session_state.widget
        st.session_state.widget = ''


    st.text_input('Enter message here ', key='widget', on_change=submit)
    # st.write(a)
    if st.session_state.something != '':
        with st.spinner("Generating response..."):

            st.session_state["messages"] += [{"role": "user", "content": st.session_state.something}]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=st.session_state["messages"]
            )

            message_response = response["choices"][0]["message"]["content"]
            st.session_state["messages"] += [
                {"role": "system", "content": message_response}
            ]
            show_messages(text)

        st.session_state.something = ''

        if st.button("Clear"):
            st.session_state["messages"] = BASE_PROMPT
            show_messages(text)


elif selected_page == "Nutrition":
    st.title("Nutrition")
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    # from pydataset import data
    from streamlit_extras.no_default_selectbox import selectbox
    import matplotlib.pyplot as plt

    st.title('Nutrition Calorie Tracker')
    df = pd.read_csv("./food.csv", encoding='mac_roman')
    ye = st.number_input('Enter Number of dishes', min_value=1, max_value=10)
    i = 0
    j = 0
    calories = 0
    list1 = []
    list2 = []

    try:
        while (i < ye):
            st.write("--------------------")
            sel = selectbox('Select the food ', df['Food'].unique(), no_selection_label=" ", key=i)
            list1.append(sel)
            sel_serving = st.number_input('Select the number of servings ', min_value=1, max_value=10, value=1, step=1,
                                          key=j + 100)
            # list2.append(sel_serving)
            i = i + 1
            j = j + 1
            st.write("Food : ", sel)
            st.write("Serving : ", sel_serving)
            st.write("Calories per serving : ", df[df['Food'] == sel]['Calories'].values[0])
            cal = df[df['Food'] == sel]['Calories'].values[0] * sel_serving
            list2.append(cal)
            st.write("Total calories for ", sel_serving, "servings of ", sel, "= ", cal, "Calories ")

            calories += cal
        st.write("--------------------")

        st.write("Total Calories:", calories)

        # Create pie chart
        fig = go.Figure(
            data=[go.Pie(labels=list1, values=list2, textinfo='label+percent', insidetextorientation='radial')])
        fig.update_layout(title="Calorie Breakdown")
        st.plotly_chart(fig)


    except:
        st.write("")

elif selected_page == "diet":
    st.title("fitness plan")

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
