import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.print("반복횟수: ");
        Scanner input = new Scanner(System.in);
        int arr[];
        int C = input.nextInt();
        for (int i = 0; i < C; i++) {
            double sum = 0;
            System.out.print("성적 개수: ");
            int N = input.nextInt();
            arr = new int[N];

            for (int j = 0; j < N; j++) {
                arr[j] = input.nextInt();
                sum += arr[j];
            }

            double avg = sum / N;
            double count = 0;

            for (int j = 0; j < N; j++) {
                if (arr[j] > avg) {
                    count++;
                }
            }
            System.out.printf("%.3f%%\n", (count / N) * 100);
        }
        input.close();
    }
}