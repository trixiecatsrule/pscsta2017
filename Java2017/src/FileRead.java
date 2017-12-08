import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class FileRead {

    private BufferedReader fileReader;

    public FileRead(String filePath) {
        try {
            FileReader reader = new FileReader(filePath);
            fileReader = new BufferedReader(reader);
            nextLine(); //Throw away the number
        } catch (IOException ex) {
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
        try {
            return fileReader.readLine();
        } catch (IOException ex) {
            ex.printStackTrace();
            return null;
        }
    }

}
