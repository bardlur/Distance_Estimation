import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)

# Initialize OpenCV face detector (Haar Cascades)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start webcam feed
cap = cv2.VideoCapture(0)

# Set the resolution (1920x1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# Real distance between the tip of the index finger (point 8) and the first joint (point 5), in cm
KNOWN_DISTANCE_CM = 8 # Adjust as per your reference measurement

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    # Check if any face is detected
    if len(faces) == 0:
        cv2.putText(frame, "You are not a human!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        for (x, y, w, h) in faces:
            # Draw a green rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Process image and find hands if a face is detected
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Store index finger positions
        index_positions = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get positions of the tips (point 8) and first joint (point 5) of index fingers
                index_tip = hand_landmarks.landmark[8]  # Point 8: tip of the index finger
                index_base = hand_landmarks.landmark[5]  # Point 5: first joint of the index finger
                h, w, _ = frame.shape

                # Convert landmark positions to pixel coordinates
                index_tip_coords = (int(index_tip.x * w), int(index_tip.y * h))
                index_base_coords = (int(index_base.x * w), int(index_base.y * h))

                # Calculate pixel distance between point 8 and point 5 of the index finger
                index_distance_pix = math.sqrt((index_tip_coords[0] - index_base_coords[0]) ** 2 + 
                                               (index_tip_coords[1] - index_base_coords[1]) ** 2)

                # Calculate the real-world distance scaling factor (cm per pixel)
                if index_distance_pix > 0:
                    cm_per_pixel = KNOWN_DISTANCE_CM / index_distance_pix

                # Add positions to list with their scaling factor
                index_positions.append((index_tip_coords, cm_per_pixel))

                # Draw landmarks for the index finger tip
                cv2.circle(frame, index_tip_coords, 10, (0, 255, 0), -1)  # Green for tip

                # Draw landmarks for the whole hand
                mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # If we have two index positions, calculate the distance
            if len(index_positions) == 2:
                point1 = index_positions[0][0]  # Hand 1 tip
                point2 = index_positions[1][0]  # Hand 2 tip

                # Draw line between the tips of the index fingers
                cv2.line(frame, point1, point2, (255, 0, 0), 2)  # Blue line

                # Calculate distance in pixels
                distance_pix = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

                # Calculate real distance in cm using the average scaling factor
                avg_cm_per_pixel = (index_positions[0][1] + index_positions[1][1]) / 2
                distance_cm = distance_pix * avg_cm_per_pixel

                # Display distance
                cv2.putText(frame, f'Distance: {distance_cm:.2f} cm', (int((point1[0] + point2[0]) / 2), 
                                int((point1[1] + point2[1]) / 2 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Display the image
    cv2.imshow('Face Detection and Finger Distance', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




