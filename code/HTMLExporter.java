import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;

public class HTMLExporter {
    public static void export(JTextArea textArea) {
        String content = textArea.getText();
        JFileChooser chooser = new JFileChooser();
        int option = chooser.showSaveDialog(null);
        if (option == JFileChooser.APPROVE_OPTION) {
            File file = chooser.getSelectedFile();
            try (PrintWriter writer = new PrintWriter(new FileWriter(file + ".html"))) {
                writer.println("<!DOCTYPE html>");
                writer.println("<html>");
                writer.println("<head>");
                writer.println("<title>Exported HTML</title>");
                writer.println("</head>");
                writer.println("<body>");
                writer.println(content);
                writer.println("</body>");
                writer.println("</html>");
                JOptionPane.showMessageDialog(null, "Exported as HTML successfully.");
            } catch (IOException e) {
                JOptionPane.showMessageDialog(null, "Error exporting as HTML: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
}
