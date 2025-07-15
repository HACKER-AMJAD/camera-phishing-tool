<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, GET, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['imgdata'])) {
    $imgData = $_POST['imgdata'];
    $imgData = str_replace('data:image/png;base64,', '', $imgData);
    $imgData = str_replace(' ', '+', $imgData);
    
    $imageData = base64_decode($imgData);

    if ($imageData === false) {
        echo json_encode(['status' => 'error', 'message' => 'Failed to decode image data']);
        exit;
    }

    $fileName = 'image_' . time() . '_' . uniqid() . '.png';
    $saveDir = 'captured_images/';

    if (!is_dir($saveDir)) {
        if (!mkdir($saveDir, 0777, true)) {
            echo json_encode(['status' => 'error', 'message' => 'Failed to create directory']);
            exit;
        }
    }

    $filePath = $saveDir . $fileName;

    if (file_put_contents($filePath, $imageData)) {
        echo json_encode(['status' => 'success', 'file' => $fileName]);
    } else {
        echo json_encode(['status' => 'error', 'message' => 'Failed to save image']);
    }
} else {
    echo json_encode(['status' => 'error', 'message' => 'Invalid request or missing data']);
}
?>
