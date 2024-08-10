<h1>Face Detection and Hand Tracking with Real-Time Distance Calculation</h1>

<p>This project is a combination of face detection using OpenCV's Haar Cascades and hand tracking using MediaPipe. It calculates the real-time distance between the tips of index fingers of both hands when a face is detected in the webcam feed.</p>



https://github.com/user-attachments/assets/54577314-8771-4ac7-95b7-17b6bc5bb920



<h2>Features</h2>

<ul>
  <li><strong>Real-Time Face Detection:</strong> Utilizes OpenCV's Haar Cascades to detect faces in the video stream.</li>
  <li><strong>Hand Tracking:</strong> Tracks both hands and identifies landmarks using MediaPipe's hand tracking solution.</li>
  <li><strong>Distance Measurement:</strong> Calculates the distance between the tips of the index fingers of both hands in real-time.</li>
  <li><strong>User Feedback:</strong> Provides a visual indicator if no face is detected in the frame.</li>
</ul>

<h2>Requirements</h2>

<ul>
  <li>Python 3.x</li>
  <li>OpenCV</li>
  <li>MediaPipe</li>
</ul>

<h2>Installation</h2>

<ol>
  <li>Clone this repository:
    <pre><code>git clone https://github.com/your_username/face-hand-tracking.git
cd face-hand-tracking</code></pre>
  </li>
  <li>Install the required packages:
    <pre><code>pip install opencv-python mediapipe</code></pre>
  </li>
  <li>Run the script:
    <pre><code>python main.py</code></pre>
  </li>
</ol>

<h2>Usage</h2>

<ul>
  <li>Ensure that your webcam is properly connected.</li>
  <li>Run the script and ensure that your face is within the camera's frame.</li>
  <li>Bring both hands into the camera's view to see the distance between your index fingers calculated in real-time.</li>
  <li>Press <code>q</code> to exit the program.</li>
</ul>

<h2>How It Works</h2>

<p>The script first detects a face using OpenCV's Haar Cascades. If a face is detected, it proceeds to track hands using MediaPipe. Hand landmarks are identified, and the distance between the tip of the index finger (point 8) and the first joint (point 5) is used as a reference to calculate real-world distances. If two hands are detected, the script calculates and displays the distance between the tips of the index fingers of both hands.</p>

<h2>Contributing</h2>

<p>Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
