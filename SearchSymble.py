import cv2

# Load the main image and the template image
main_image_path = 'main_image.png'
template_path = 'symbol_template.png'

main_image = cv2.imread(main_image_path)
template = cv2.imread(template_path)

# Convert both images to grayscale
main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Get the width and height of the template
w, h = template_gray.shape[::-1]

# Perform template matching
result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# Define a threshold to determine a match
threshold = 0.8
locations = cv2.minMaxLoc(result)

# Get the best match position
_, max_val, _, max_loc = cv2.minMaxLoc(result)

if max_val >= threshold:
    print(f"Symbol found at location: {max_loc} with matching confidence: {max_val:.2f}")
    # Draw a rectangle around the matched region
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(main_image, top_left, bottom_right, (0, 255, 0), 2)
else:
    print("Symbol not found with sufficient confidence.")

# Display the result
cv2.imshow('Detected Symbol', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
