<?php
include('conexion.php');

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $documento = $_POST['documento'];
    $tipoDocumento = $_POST['tipoDocumento'];
    $nombres = $_POST['nombres'];
    $apellidos = $_POST['apellidos'];
    $genero = $_POST['genero'];
    $celular = $_POST['celular'];
    $correo = $_POST['correo'];
    $fechaNacimiento = $_POST['fechaNacimiento'];

    $sql = "INSERT INTO usuarios (documento, tipo_documento, nombres, apellidos, genero, celular, correo, fecha_nacimiento)
            VALUES ('$documento', '$tipoDocumento', '$nombres', '$apellidos', '$genero', '$celular', '$correo', '$fechaNacimiento')";

    if ($conn->query($sql) === TRUE) {
        echo "Información guardada correctamente";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

$conn->close();
?>
