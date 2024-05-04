import java.awt.BorderLayout;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.SwingUtilities;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;

public class NoteManager {
    private JFrame parentFrame; // Tham chiếu tới cửa sổ chính của ứng dụng
    private JTextArea currentTextArea; // JTextArea hiện tại để hiển thị nội dung file note

    public NoteManager(JFrame parentFrame) {
        this.parentFrame = parentFrame;
    }

    public void openNote() {
        JFileChooser fileChooser = new JFileChooser();
        int option = fileChooser.showOpenDialog(parentFrame);

        if (option == JFileChooser.APPROVE_OPTION) {
            File file = fileChooser.getSelectedFile();
            SwingUtilities.invokeLater(new Runnable() {
                @Override
                public void run() {
                    JFrame noteFrame = new JFrame("Note: " + file.getName());
                    JTextArea textArea = new JTextArea();
                    JScrollPane scrollPane = new JScrollPane(textArea);
                    noteFrame.getContentPane().add(scrollPane, BorderLayout.CENTER);

                    try {
                        BufferedReader reader = new BufferedReader(new FileReader(file));
                        String line;
                        while ((line = reader.readLine()) != null) {
                            textArea.append(line + "\n");
                        }
                        reader.close();
                    } catch (IOException ex) {
                        ex.printStackTrace();
                    }

                    noteFrame.setSize(600, 400); // Thiết lập kích thước của cửa sổ noteFrame
                    noteFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE); // Thiết lập hành động khi đóng cửa sổ
                    noteFrame.setVisible(true);

                    // Nếu đã có một JTextArea hiện tại, hãy đảm bảo rằng JTextArea mới cũng sẽ nhận
                    // được các sự kiện DocumentListener từ JTextArea hiện tại
                    if (currentTextArea != null) {
                        textArea.getDocument().addDocumentListener(new DocumentListener() {
                            @Override
                            public void insertUpdate(DocumentEvent e) {
                                try {
                                    currentTextArea.getDocument().insertString(e.getOffset(),
                                            e.getDocument().getText(e.getOffset(), e.getLength()), null);
                                } catch (Exception ex) {
                                    ex.printStackTrace();
                                }
                            }

                            @Override
                            public void removeUpdate(DocumentEvent e) {
                                try {
                                    currentTextArea.getDocument().remove(e.getOffset(), e.getLength());
                                } catch (Exception ex) {
                                    ex.printStackTrace();
                                }
                            }

                            @Override
                            public void changedUpdate(DocumentEvent e) {
                                // Do nothing
                            }
                        });
                    }
                    currentTextArea = textArea;
                }
            });
        }
    }
}

