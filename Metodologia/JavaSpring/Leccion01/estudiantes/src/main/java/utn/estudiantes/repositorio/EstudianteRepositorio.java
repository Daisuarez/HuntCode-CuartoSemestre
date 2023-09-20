package utn.estudiantes.repositorio;
import org.springframework.data.jpa.repository.JpaRepository; // no hace falta agregar anotaciones con esto
import utn.estudiantes.modelo.estudiantes2022;
public interface EstudianteRepositorio extends JpaRepository<estudiantes2022,Integer> { // con esta interface nos garantizamos todos los metdos por utilizar en la app


}
