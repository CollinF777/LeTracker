import cv2
import mediapipe as mp

# Set stats for the face mesh
face_mesh = mp.solutions.face_mesh.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_faces=1
)

# Open up the webcam
cam = cv2.VideoCapture(0)

# Threshold values for expression detection
eye_opening_thresh = 0.03
mouth_open_thresh = 0.05
squinting_thresh = 0.02

# LeBron scream if you love
def leSatan(face_lm_pt):
    # Lip Landmarks (center of upper and lower lips)
    top_lip = face_lm_pt.landmark[13]
    btm_lip = face_lm_pt.landmark[14]

    mouth_open = abs(top_lip.y - btm_lip.y)

    # Check for wide open mouth
    return mouth_open > mouth_open_thresh

# LeBron big grin
def leGrin(face_lm_pt):
    # Get eye landmarks
    l_top = face_lm_pt.landmark[159]
    l_bot = face_lm_pt.landmark[145]

    r_top = face_lm_pt.landmark[386]
    r_bot = face_lm_pt.landmark[374]

    eye_opening = (abs(l_top.y - l_bot.y) + abs(r_top.y - r_bot.y)) / 2.0

    # Check for wide open eyes
    return eye_opening > eye_opening_thresh

def leLockedIn(face_lm_pt):
    # Get eye landmarks
    l_top = face_lm_pt.landmark[159]
    l_bot = face_lm_pt.landmark[145]

    r_top = face_lm_pt.landmark[386]
    r_bot = face_lm_pt.landmark[374]

    squint = (abs(l_top.y - l_bot.y) + abs(r_top.y - r_bot.y)) / 2.0

    # Check for squinting eyes
    return squint < squinting_thresh

def main():
    while True:
        # Get frame from webcam
        ret, image = cam.read()

        # If the camera is unreadable, exit
        if not ret:
            break

        # Flip image for mirror effect
        image = cv2.flip(image, 1)

        # Frame dimensions
        height, width, depth = image.shape

        # Process face detection
        rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        processed_img = face_mesh.process(rgb_img)
        face_lm_pt = processed_img.multi_face_landmarks

        # Default img
        leBron = "LeImages/lebron_serious.jpg"

        # Check for face detection
        if face_lm_pt:
            face_lm_pt = face_lm_pt[0]

            # Match to images
            if leSatan(face_lm_pt):
                leBron = "LeImages/lebron_scream_if_you_love.jpg"
            elif leGrin(face_lm_pt):
                leBron = "LeImages/lebron_grin.jpg"
            elif leLockedIn(face_lm_pt):
                leBron = "LeImages/lebron_locked_in.jpg"
            else:
                leBron = "LeImages/lebron_serious.jpg"

            # Draw face landmarks on camera feed
            height, width = image.shape[:2]

            # Loop through the 468 landmarks
            for lm in face_lm_pt.landmark:
                # Convert to pixel cords
                x = int(lm.x * width)
                y = int(lm.y * height)

                cv2.circle(image, (x,y), 1, (0, 100, 0), -1)

        # Display camera feed window
        cv2.imshow("LeTracker", image)

        # Load and display LeBron
        leGoat = cv2.imread(leBron)

        # Check that image loaded correctly
        if leGoat is not None:
            leGoat = cv2.resize(leGoat, (640, 480))
            cv2.imshow("Live LeBron Reaction", leGoat)
        # Display black image otherwise
        else:
            blank = image * 0

            # Error text
            cv2.putText(blank, f"Missing: {leBron}", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("Live LeBron Reaction", blank)

        # Make exit key esc
        key = cv2.waitKey(1)
        if key == 27:
            break

    # Cleanup
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()