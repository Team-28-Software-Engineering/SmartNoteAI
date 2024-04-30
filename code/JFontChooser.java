import javax.swing.*;
import java.awt.*;
import java.awt.font.TextAttribute;
import java.util.Map;

public class JFontChooser {
    public static Font showDialog(Component parentComponent, String title, Font defaultFont) {
        // Danh sách các kiểu chữ có sẵn trên hệ thống
        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
        String[] fontNames = ge.getAvailableFontFamilyNames();

        // Hiển thị danh sách kiểu chữ cho người dùng chọn
        String selectedFontName = (String) JOptionPane.showInputDialog(parentComponent, "Choose Font:",
                title, JOptionPane.PLAIN_MESSAGE, null, fontNames, defaultFont.getFontName());

        // Nếu người dùng đã chọn kiểu chữ, trả về font tương ứng
        if (selectedFontName != null) {
            return new Font(selectedFontName, defaultFont.getStyle(), defaultFont.getSize());
        } else {
            // Người dùng không chọn kiểu chữ, trả về font mặc định
            return defaultFont;
        }
    }
}
