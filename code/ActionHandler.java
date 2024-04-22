import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import javax.swing.JFileChooser;
import javax.swing.JTextArea;

public class ActionHandler implements ActionListener {
    private JTextArea textArea;
    private JFileChooser fileChooser;
    private String currentFile;

    public ActionHandler(JTextArea textArea, JFileChooser fileChooser) {
        this.textArea = textArea;
        this.fileChooser = fileChooser;
    }

    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();
        if (command.equals("New")) {
            textArea.setText("");
            currentFile = null;
        } else if (command.equals("Open")) {
            int returnVal = fileChooser.showOpenDialog(null);
            if (returnVal == JFileChooser.APPROVE_OPTION) {
                File file = fileChooser.getSelectedFile();
                try {
                    FileReader reader = new FileReader(file);
                    textArea.read(reader, null);
                    reader.close();
                    currentFile = file.getAbsolutePath();
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
        } else if (command.equals("Save")) {
            if (currentFile != null) {
                try {
                    FileWriter writer = new FileWriter(currentFile);
                    textArea.write(writer);
                    writer.close();
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            } else {
                SaveAsDialog saveAsDialog = new SaveAsDialog(null, textArea.getText());
                currentFile = saveAsDialog.getCurrentFile();
            }
        } else if (command.equals("Save As")) {
            SaveAsDialog saveAsDialog = new SaveAsDialog(null, textArea.getText());
            currentFile = saveAsDialog.getCurrentFile();
        }
    }
}
