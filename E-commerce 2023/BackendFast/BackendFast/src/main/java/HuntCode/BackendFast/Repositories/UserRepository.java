package HuntCode.BackendFast.Repositories;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import lombok.Data;

@Data
@Entity(name = "users")
public class User {
    @Column(name = "id")
    @Id
    @GeneratedValue(strategy = jakarta.persistence.GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    @Column(name = "email")
    private String email;
    @Column(name = "password")
    private String password;
    @Column(name = "password_confirmation")
    private String passwordConfirmation;
    @Column(name = "role")
    private String role;

}
