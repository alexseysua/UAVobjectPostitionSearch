import cv2
sift = cv2.SIFT_create()
bf = cv2.BFMatcher()

def findMatches(photoPath, tilesMap):
    userPhoto = cv2.imread(photoPath, cv2.IMREAD_COLOR)
    keypointsUser, descriptorsUser = sift.detectAndCompute(userPhoto, None)

    for tile in tilesMap:
        keypoints_tile, descriptors_tile = sift.detectAndCompute(tile[1], None)
        matches = bf.knnMatch(descriptorsUser, descriptors_tile, k=2)

        good_matches = []
        for m, n in matches:
            if m.distance < 0.5 * n.distance:
                good_matches.append(m)
        matching_ratio = len(good_matches) / len(keypointsUser)
        tile[2] = matching_ratio
    sorted_data = sorted(tilesMap, key=lambda x: x[2])

    best_match = sorted_data[-1]
    lowest_match = sorted_data[0]

    result = {
        "photo_path": photoPath,
        "highest_ratio_match": (best_match[0], best_match[2]),
        "lowest_ratio_match": (lowest_match[0], lowest_match[2])
    }

    return result