import java.util.Scanner;
public class whiles
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the number of rows:");
        int rows = scan.nextInt();
        int times = 1;
        String stars = "*";
        do {
            System.out.println(stars);
            stars = stars + "*";
            times+=1;
        } while (times <= rows);
        scan.close();
    }
}