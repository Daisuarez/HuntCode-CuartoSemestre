package utn.estudiantes.modelo;

import jakarta.persistence.Entity;  //indica que esta clase es clase entidad que represanta una tabla de datos, va con lo de abajo
import jakarta.persistence.GeneratedValue; //para como generar las llaves
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id; //importa el id de la tabla
import lombok.AllArgsConstructor;
import lombok.Data; // crea los metodos get y set
import lombok.NoArgsConstructor;
import lombok.ToString;

@Entity // Boilerplate - codigo repetitivo lo simplificamos con las importaciones de abajo a travez de LOOMBOK
@Data // crea los metodos get y set
@NoArgsConstructor // agrega el constructor vacio, sin argumentos
@AllArgsConstructor // constructor con todos los argumentos
@ToString // el viejo pero confiable to string ajja


public class estudiantes2022 {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // como se genera el valor de la llave primaria , de forma autoincrementable
    private Integer idestudiantes2022;
    private String nombre;
    private String apellido;
    private String telefono;
    private String email;



}
