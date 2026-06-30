module com.example.app_classifier {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.app_classifier to javafx.fxml;
    exports com.example.app_classifier;
}