<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uploader et Modifier un Fichier Excel</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }
        h1 {
            color: #ff7043;
            margin-bottom: 20px;
        }
        .container {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            max-width: 500px;
            width: 100%;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            font-size: 1.2em;
            margin-bottom: 10px;
            color: #ff5722;
        }
        input[type="file"] {
            margin-bottom: 20px;
            padding: 10px;
            border: 2px solid #ccc;
            border-radius: 25px;
            background-color: #e0e0e0;
            color: #333;
            font-size: 1em;
            cursor: pointer;
        }
        input[type="file"]::file-selector-button {
            background-color: #b0bec5;
            border: none;
            border-radius: 25px;
            color: #fff;
            padding: 10px 20px;
            font-size: 1em;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        input[type="file"]::file-selector-button:hover {
            background-color: #90a4ae;
        }
        input[type="submit"] {
            padding: 10px 20px;
            border: none;
            border-radius: 25px;
            background-color: #ff5722;
            color: #fff;
            font-size: 1.1em;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        input[type="submit"]:hover {
            background-color: #e64a19;
        }
        .footer {
            margin-top: 20px;
            font-size: 0.9em;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Uploader un fichier Excel</h1>
        <form action="/src/upload.php" method="post" enctype="multipart/form-data">
            <label for="file">Sélectionner un fichier Excel :</label>
            <input type="file" name="file" id="file" accept=".xlsx">
            <input type="submit" value="Uploader">
        </form>
    </div>
    <div class="footer">
        <p>&copy; 2024 Votre Entreprise. Tous droits réservés.</p>
    </div>
</body>
</html>
