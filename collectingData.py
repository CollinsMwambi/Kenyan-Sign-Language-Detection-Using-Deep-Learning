import cv2
import numpy as np
import os

# Creating folders for Eshara data
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/A")
    os.makedirs("data/train/B")
    os.makedirs("data/train/C")
    os.makedirs("data/train/D")
    os.makedirs("data/train/E")
    os.makedirs("data/train/F")
    os.makedirs("data/train/G")
    os.makedirs("data/train/H")
    os.makedirs("data/train/I")
    os.makedirs("data/train/J")
    os.makedirs("data/train/K")
    os.makedirs("data/train/L")
    os.makedirs("data/train/M")
    os.makedirs("data/train/N")
    os.makedirs("data/train/O")
    os.makedirs("data/train/P")
    os.makedirs("data/train/Q")
    os.makedirs("data/train/R")
    os.makedirs("data/train/S")
    os.makedirs("data/train/T")
    os.makedirs("data/train/U")
    os.makedirs("data/train/V")
    os.makedirs("data/train/W")
    os.makedirs("data/train/X")
    os.makedirs("data/train/Y")
    os.makedirs("data/train/Z")
    os.makedirs("data/test/A")
    os.makedirs("data/test/B")
    os.makedirs("data/test/C")
    os.makedirs("data/test/D")
    os.makedirs("data/test/E")
    os.makedirs("data/test/F")
    os.makedirs("data/test/G")
    os.makedirs("data/test/H")
    os.makedirs("data/test/I")
    os.makedirs("data/test/J")
    os.makedirs("data/test/K")
    os.makedirs("data/test/L")
    os.makedirs("data/test/M")
    os.makedirs("data/test/N")
    os.makedirs("data/test/O")
    os.makedirs("data/test/P")
    os.makedirs("data/test/Q")
    os.makedirs("data/test/R")
    os.makedirs("data/test/S")
    os.makedirs("data/test/T")
    os.makedirs("data/test/U")
    os.makedirs("data/test/V")
    os.makedirs("data/test/W")
    os.makedirs("data/test/X")
    os.makedirs("data/test/Y")
    os.makedirs("data/test/Z")
    
    

# Train or test to capture data you want,depending on the mode
mode = 'train'
directory = 'data/'+mode+'/'

#Images are captured from the webcam using the cv2.VideoCapture() function 
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # initializing count dictionary to keep track of images in each folder
    count = {'A': len(os.listdir(directory+"/A")),
             'B': len(os.listdir(directory+"/B")),
             'C': len(os.listdir(directory+"/C")),
             'D': len(os.listdir(directory+"/D")),
             'E': len(os.listdir(directory+"/E")),
             'F': len(os.listdir(directory+"/F")),
             'G': len(os.listdir(directory+"/G")),
             'H': len(os.listdir(directory+"/H")),
             'I': len(os.listdir(directory+"/I")),
             'J': len(os.listdir(directory+"/J")),
             'K': len(os.listdir(directory+"/K")),
             'L': len(os.listdir(directory+"/L")),
             'M': len(os.listdir(directory+"/M")),
             'N': len(os.listdir(directory+"/N")),
             'O': len(os.listdir(directory+"/O")),
             'P': len(os.listdir(directory+"/P")),
             'Q': len(os.listdir(directory+"/Q")),
             'R': len(os.listdir(directory+"/R")),
             'S': len(os.listdir(directory+"/S")),
             'T': len(os.listdir(directory+"/T")),
             'U': len(os.listdir(directory+"/U")),
             'V': len(os.listdir(directory+"/V")),
             'W': len(os.listdir(directory+"/W")),
             'X': len(os.listdir(directory+"/X")),
             'Y': len(os.listdir(directory+"/Y")),
             'Z': len(os.listdir(directory+"/Z"))

             
             }
    
    # Printing the count in each set to the screen
    cv2.putText(frame, "Collecting : "+mode, (10, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)
    cv2.putText(frame, "NO. OF IMAGES", (10, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,100), 2)
    cv2.putText(frame, "A : "+str(count['A']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "B : "+str(count['B']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "C : "+str(count['C']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "D : "+str(count['D']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "E : "+str(count['E']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "F : "+str(count['F']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "G : "+str(count['G']), (70, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "H : "+str(count['H']), (70, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "I : "+str(count['I']), (70, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "J : "+str(count['J']), (70, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "K : "+str(count['K']), (70, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "L : "+str(count['L']), (70, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "M : "+str(count['M']), (130, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "N : "+str(count['N']), (130, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "O : "+str(count['O']), (130, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "P : "+str(count['P']), (130, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "Q : "+str(count['Q']), (130, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "R : "+str(count['R']), (130, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "S : "+str(count['S']), (190, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "T : "+str(count['T']), (190, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "U : "+str(count['U']), (190, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "V : "+str(count['V']), (190, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "W : "+str(count['W']), (190, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "X : "+str(count['X']), (190, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "Y : "+str(count['Y']), (250, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, "Z : "+str(count['Z']), (250, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
   
    # Coordinates of the Region of interest
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64)) 
     
         #cv2.imshow is used for display
    cv2.imshow("Frame", frame)
   #changing image collected to black and white
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('A'):
        cv2.imwrite(directory+'A/'+str(count['A'])+'.jpg', roi)
    if interrupt & 0xFF == ord('B'):
        cv2.imwrite(directory+'B/'+str(count['B'])+'.jpg', roi)
    if interrupt & 0xFF == ord('C'):
        cv2.imwrite(directory+'C/'+str(count['C'])+'.jpg', roi)
    if interrupt & 0xFF == ord('D'):
        cv2.imwrite(directory+'D/'+str(count['D'])+'.jpg', roi)
    if interrupt & 0xFF == ord('E'):
        cv2.imwrite(directory+'E/'+str(count['E'])+'.jpg', roi)
    if interrupt & 0xFF == ord('F'):
        cv2.imwrite(directory+'F/'+str(count['F'])+'.jpg', roi)
    if interrupt & 0xFF == ord('G'):
        cv2.imwrite(directory+'G/'+str(count['G'])+'.jpg', roi)
    if interrupt & 0xFF == ord('H'):
        cv2.imwrite(directory+'H/'+str(count['H'])+'.jpg', roi)
    if interrupt & 0xFF == ord('I'):
        cv2.imwrite(directory+'I/'+str(count['I'])+'.jpg', roi)
    if interrupt & 0xFF == ord('J'):
        cv2.imwrite(directory+'J/'+str(count['J'])+'.jpg', roi)
    if interrupt & 0xFF == ord('K'):
        cv2.imwrite(directory+'K/'+str(count['K'])+'.jpg', roi)
    if interrupt & 0xFF == ord('L'):
        cv2.imwrite(directory+'L/'+str(count['L'])+'.jpg', roi)
    if interrupt & 0xFF == ord('M'):
        cv2.imwrite(directory+'M/'+str(count['M'])+'.jpg', roi)
    if interrupt & 0xFF == ord('N'):
        cv2.imwrite(directory+'N/'+str(count['N'])+'.jpg', roi)
    if interrupt & 0xFF == ord('O'):
        cv2.imwrite(directory+'O/'+str(count['O'])+'.jpg', roi)
    if interrupt & 0xFF == ord('P'):
        cv2.imwrite(directory+'P/'+str(count['P'])+'.jpg', roi)
    if interrupt & 0xFF == ord('Q'):
        cv2.imwrite(directory+'Q/'+str(count['Q'])+'.jpg', roi)
    if interrupt & 0xFF == ord('R'):
        cv2.imwrite(directory+'R/'+str(count['R'])+'.jpg', roi)
    if interrupt & 0xFF == ord('S'):
        cv2.imwrite(directory+'S/'+str(count['S'])+'.jpg', roi)
    if interrupt & 0xFF == ord('T'):
        cv2.imwrite(directory+'T/'+str(count['T'])+'.jpg', roi)
    if interrupt & 0xFF == ord('U'):
        cv2.imwrite(directory+'U/'+str(count['U'])+'.jpg', roi)
    if interrupt & 0xFF == ord('V'):
        cv2.imwrite(directory+'V/'+str(count['V'])+'.jpg', roi)
    if interrupt & 0xFF == ord('W'):
        cv2.imwrite(directory+'W/'+str(count['W'])+'.jpg', roi)
    if interrupt & 0xFF == ord('X'):
        cv2.imwrite(directory+'X/'+str(count['X'])+'.jpg', roi)
    if interrupt & 0xFF == ord('Y'):
        cv2.imwrite(directory+'Y/'+str(count['Y'])+'.jpg', roi)
    if interrupt & 0xFF == ord('Z'):
        cv2.imwrite(directory+'Z/'+str(count['Z'])+'.jpg', roi)
   
cap.release()

cv2.destroyAllWindows()
