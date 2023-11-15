<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $busqueda = $_POST["busqueda"];

    // Conecta a la base de datos
    $conexion = new mysqli("localhost", "root", "", "base_de_prueba");

    if ($conexion->connect_error) {
        die("Error de conexión: " . $conexion->connect_error);
    }

    $sql1 = "SELECT cod_paciente FROM pacientes WHERE dni LIKE '%$busqueda'";
    $resultadoCod = $conexion->query($sql1);

    if ($resultadoCod->num_rows > 0) {
        // Extrae el valor de la consulta
        $row = $resultadoCod->fetch_assoc();
        $cod_paciente = $row['cod_paciente'];

        // Realiza la búsqueda en la base de datos
        $sql = "SELECT t.fecha, t.hora, t.paciente, m.Mapellido FROM turnos t INNER JOIN medicos m ON t.medico = m.cod_medico WHERE t.paciente = $cod_paciente";

        $resultado = $conexion->query($sql);
    }
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;300;400;600;900&display=swap" rel="stylesheet"/>
        <link rel="stylesheet" href="../css/style.css"/>
        <link rel="icon" type="image/png" href="../assets/img/clinet1.png">
        <title>Resultados</title>
    </head>
    <body>
        <header class="header">
            <nav class="nav container" id="nav">
                <a href="../index.html"><img src="../assets/img/clinet1.png" alt="Logo Clinet" class="nav_logo"></a>
                <ul class="nav_list">
                    <li class="nav_item"><a href="../index.html" class="nav_link">Inicio</a></li>
                    <li class="nav_item"><a href="../pages/nosotros.html" class="nav_link">Nosotros</a></li>
                    <li class="nav_item"><a href="../pages/consulta.html" class="nav_link">Consultar Turnos</a></li>
                    <li class="nav_item"><a href="../pages/contacto.html" class="nav_link">Contacto</a></li>
                </ul>
                <a href="#nav" class="nav_hamburguesa">
                    <img src="../assets/menu.svg" alt="" class="nav_icon" />
                </a>
                <a href="#" class="nav_cruz">
                    <img src="../assets/close.svg" alt="" class="nav_icon" />
                </a>
            </nav>
        </header>
        <main class="main-consulta-php">
            <?php
            if (isset($resultado) && $resultado !== false && $resultado->num_rows > 0) {
                ?>
                <table>
                    <tr>
                        <th>Fecha</th>
                        <th>Hora</th>
                        <th>Paciente</th>
                        <th>Medico</th>
                    </tr>
                    <?php
                    while ($fila = $resultado->fetch_assoc()) {
                        ?>
                        <tr>
                            <td><?php echo $fila["fecha"] ?></td>
                            <td><?php echo $fila["hora"] ?></td>
                            <td><?php echo $fila["paciente"] ?></td>
                            <td><?php echo $fila["Mapellido"] ?></td>
                        </tr>
                        <?php
                    }
                    ?>
                </table>
                <?php
            } else {
                ?>
                <h3>No se encontraron resultados.</h3>
                <?php
            }
            ?>
        </main>
        <footer class="footer">
            <ul class="menu">
                <li class="menu__item"><a class="menu__link" href="../index.html">Inicio</a></li>
                <li class="menu__item"><a class="menu__link" href="../pages/nosotros.html">Nosotros</a></li>
                <li class="menu__item"><a class="menu__link" href="../pages/consulta.html">Consultas</a></li>
                <li class="menu__item"><a class="menu__link" href="../pages/contacto.html">Contacto</a></li>
            </ul>
            <p>&copy;2023 Clinet | Todos los derechos reservados</p>
        </footer>
    </body>
    </html>
    <?php
    $conexion->close();
}
?>