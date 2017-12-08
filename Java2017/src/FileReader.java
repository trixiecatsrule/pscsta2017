import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileReader {

    private Scanner scanner;

    public FileReader(String filePath) {
        try {
            scanner = new Scanner(new File(filePath));
            int num = scanner.nextInt();
            scanner.nextLine(); //Throw away the number
        } catch (FileNotFoundException ex) {
            ex.printStackTrace();
        }
    }

    //When reading in data from the text file into x, use:
    //    	x = file.nextInt()
    //    	x = file.nextDouble()
    //    	x = file.nextLine()

    //int y = Integer.parseInt(“34”); will turn “34” into an int
    //double x = Double.parseDouble(“2.1”); will turn “2.1” into a double

    public String nextLine() {
        return scanner.nextLine();
    }

}
