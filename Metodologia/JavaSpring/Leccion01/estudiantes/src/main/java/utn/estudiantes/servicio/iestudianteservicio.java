package utn.estudiantes.servicio;
import utn.estudiantes.modelo.estudiantes2022;
import java.util.List;
public interface iestudianteservicio {
    public List<estudiantes2022> listarEstudiantes();
    public estudiantes2022 buscarEstudiantePorId(Integer idEstudiante);
    public void guardarEstudiante( estudiantes2022 estudiante);
    public void eliminarEstudiante(estudiantes2022 estudiante);
}
