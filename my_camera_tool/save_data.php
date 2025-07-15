<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, GET, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");

$response = ['status' => 'error', 'message' => 'Invalid request or missing data'];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $saveDir = 'captured_data/';

    if (!is_dir($saveDir)) {
        if (!mkdir($saveDir, 0777, true)) {
            $response['message'] = 'Failed to create directory';
            echo json_encode($response);
            exit;
        }
    }

    $uniqueId = time() . '_' . uniqid();
    $savedFiles = [];

    // --- Handle Image Data ---
    if (isset($_POST['imgdata'])) {
        $imgData = $_POST['imgdata'];
        $imgData = str_replace('data:image/png;base64,', '', $imgData);
        $imgData = str_replace(' ', '+', $imgData);
        
        $imageData = base64_decode($imgData);

        if ($imageData !== false) {
            $imageFileName = 'image_' . $uniqueId . '.png';
            $imageFilePath = $saveDir . $imageFileName;
            if (file_put_contents($imageFilePath, $imageData)) {
                $savedFiles['image'] = $imageFileName;
            } else {
                $response['message'] = 'Failed to save image';
            }
        } else {
            $response['message'] = 'Failed to decode image data';
        }
    }

    // --- Handle Video Data ---
    if (isset($_FILES['videoFile']) && $_FILES['videoFile']['error'] === UPLOAD_ERR_OK) {
        $videoTmpPath = $_FILES['videoFile']['tmp_name'];
        // Use uploaded file's original name to get extension, or force webm
        $videoFileName = 'video_' . $uniqueId . '.webm'; 
        $videoFilePath = $saveDir . $videoFileName;

        if (move_uploaded_file($videoTmpPath, $videoFilePath)) {
            $savedFiles['video'] = $videoFileName;
        } else {
            $response['message'] = (isset($response['message']) ? $response['message'] . ' and ' : '') . 'Failed to save video';
        }
    }

    if (!empty($savedFiles)) {
        $response['status'] = 'success';
        $response['message'] = 'Data saved successfully';
        $response['files'] = $savedFiles;
    }
}

echo json_encode($response);
?>
