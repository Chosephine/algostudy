public class solve001 {

    public int solution(int num1, int num2) {
        int answer = num1 % num2;
        return answer;
    }

    public static void main(String[] args) {
        solve001 s = new solve001();
        int result = s.solution(3, 2);
        System.out.println(result);
    }

}
