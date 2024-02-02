<?php
include('conexion.php');

if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    $documentoBuscar = $_GET['documento'];

    $sql = "SELECT * FROM usuarios WHERE documento = '$documentoBuscar'";
    $resultado = $conn->query($sql);

    if ($resultado->num_rows > 0) {
        // Datos encontrados
        $fila = $resultado->fetch_assoc();
        $informacion = array(
            'documento' => $fila['documento'],
            'tipoDocumento' => $fila['tipo_documento'],
            'nombres' => $fila['nombres'],
            'apellidos' => $fila['apellidos'],
            'genero' => $fila['genero'],
            'celular' => $fila['celular'],
            'correo' => $fila['correo'],
            'fechaNacimiento' => $fila['fecha_nacimiento']
        );

        echo json_encode(array('encontrado' => true, 'informacion' => $informacion));
    } else {
        // Datos no encontrados
        echo json_encode(array('encontrado' => false));
    }
}

$conn->close();
?>
