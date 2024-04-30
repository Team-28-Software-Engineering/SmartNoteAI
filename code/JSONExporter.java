import javax.swing.*;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;

public class JSONExporter {
    private final Map<String, Object> map;

    public JSONExporter() {
        map = new HashMap<>();
    }

    public void put(String key, Object value) {
        map.put(key, value);
    }

    public Object get(String key) {
        return map.get(key);
    }

    public String toJSONString() {
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        boolean first = true;
        for (Map.Entry<String, Object> entry : map.entrySet()) {
            if (!first) {
                sb.append(", ");
            }
            sb.append("\"").append(entry.getKey()).append("\": ");
            Object value = entry.getValue();
            if (value instanceof String) {
                sb.append("\"").append(value).append("\"");
            } else {
                sb.append(value);
            }
            first = false;
        }
        sb.append("}");
        return sb.toString();
    }

    public static void export(JTextArea textArea) {
        String content = textArea.getText();
        JFileChooser chooser = new JFileChooser();
        int option = chooser.showSaveDialog(null);
        if (option == JFileChooser.APPROVE_OPTION) {
            File file = chooser.getSelectedFile();
            try (PrintWriter writer = new PrintWriter(new FileWriter(file + ".json"))) {
                JSONExporter exporter = new JSONExporter();
                exporter.put("content", content);
                writer.println(exporter.toJSONString());
                JOptionPane.showMessageDialog(null, "Exported as JSON successfully.");
            } catch (IOException e) {
                JOptionPane.showMessageDialog(null, "Error exporting as JSON: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
}
