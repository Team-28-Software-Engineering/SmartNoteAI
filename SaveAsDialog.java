import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import javax.swing.JFileChooser;
import javax.swing.JFrame;

public class SaveAsDialog {
    private String currentFile;

    public SaveAsDialog(JFrame parentFrame, String content) {
        JFileChooser fileChooser = new JFileChooser();
        int returnVal = fileChooser.showSaveDialog(parentFrame);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            File file = fileChooser.getSelectedFile();
            try {
                FileWriter writer = new FileWriter(file);
                writer.write(content);
                writer.close();
                currentFile = file.getAbsolutePath();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }

    public String getCurrentFile() {
        return currentFile;
    }
}
