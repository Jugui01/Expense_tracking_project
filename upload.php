<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];
    $uploadDir = 'uploads/';
    $uploadFile = $uploadDir . basename($file['name']);

    // Vérifier si le fichier a été téléchargé sans erreur
    if ($file['error'] == UPLOAD_ERR_OK) {
        // Créer le dossier de destination s'il n'existe pas
        if (!is_dir($uploadDir)) {
            mkdir($uploadDir, 0755, true);
        }

        // Déplacer le fichier téléchargé dans le dossier de destination
        if (move_uploaded_file($file['tmp_name'], $uploadFile)) {
            echo "Le fichier " . basename($file['name']) . " a été téléchargé avec succès.<br>";

            // Commande pour exécuter le script Python
            $command = escapeshellcmd("python modify_excel.py " . escapeshellarg($uploadFile));
            $output = shell_exec($command . ' 2>&1'); // Capture les erreurs aussi

            // Afficher la sortie du script Python
            if ($output === null) {
                echo "Erreur lors de l'exécution du script Python.<br>";
            } else {
                echo "<pre>$output</pre>";
            }

            echo "<a href='$uploadFile'>Télécharger le fichier modifié</a>";
        } else {
            echo "Erreur lors du déplacement du fichier.";
        }
    } else {
        echo "Erreur lors du téléchargement du fichier.";
    }
} else {
    echo "Aucun fichier n'a été téléchargé.";
}
?>
