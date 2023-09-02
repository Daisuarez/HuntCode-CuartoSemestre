package utn.estudiantes.servicio;
import
public interface iestudianteservicio {
    public List<Estudiante> listarEstudiantes();
    public Estudiante buscarEstudiantePorId(Integer idEstudiante);
    public void guardarEstudiante( Estudiante estudiante);
    public void eliminarEstudiante(Estudiante estudiante);
}
