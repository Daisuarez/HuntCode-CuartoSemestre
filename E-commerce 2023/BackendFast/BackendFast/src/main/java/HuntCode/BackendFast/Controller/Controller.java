package HuntCode.BackendFast.Controller;

import org.apache.catalina.User;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1")
public class UserController {

    private final UserController userService;

    public UserController(userService userService){
        this.userService = userService;

    @GetMapping(value = "/")
    public @ResponseBody list<User> getAll() {return userService.findAll()}
    }
}







