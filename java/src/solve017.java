import java.util.Scanner;

/*
 * programmers 코딩테스트 입문
 * 직각삼각형 출력하기
*/

public class solve017{

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i=1; i <= n; i++) {
        	for (int j=1; j <= i; j++) {System.out.printf("*");}
	    	System.out.println();
        }
    }
}
