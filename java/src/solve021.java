
/*
 * programmers 코딩테스트 입문
 * 양꼬치
*/

public class solve021{
	
	public static int solution(int n, int k) {
		// 양꼬치 n인분, 음료수 k개
		// 양꼬치 10인분 먹으면 음료수 1개 서비스
		int service = n / 10;
        int answer = 12000 * n + 2000 * (k - service);
        return answer;
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int inPut1 = 64;
    	int inPut2 = 6;
    	int answer = solution(inPut1, inPut2);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    }
}
