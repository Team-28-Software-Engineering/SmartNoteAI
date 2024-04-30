import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;

public class XMLExporter {
    public static void export(JTextArea textArea) {
        String content = textArea.getText();
        JFileChooser chooser = new JFileChooser();
        int option = chooser.showSaveDialog(null);
        if (option == JFileChooser.APPROVE_OPTION) {
            File file = chooser.getSelectedFile();
            try (PrintWriter writer = new PrintWriter(new FileWriter(file + ".xml"))) {
                writer.println("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
                writer.println("<document>");
                writer.println("<content>");
                writer.println(content);
                writer.println("</content>");
                writer.println("</document>");
                JOptionPane.showMessageDialog(null, "Exported as XML successfully.");
            } catch (IOException e) {
                JOptionPane.showMessageDialog(null, "Error exporting as XML: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
}
