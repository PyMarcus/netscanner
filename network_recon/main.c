#include <stdio.h>


int isPrime(int num){
    // verifica se é primo
    int count = 0;
    for(int i=1; i < num; i++){
        if(num % i == 0){
            count++;
        }
        if(count == 2){
            printf("\nNao e");
            return 0;
        }
    }printf("\ne");
    return num;
}

int isPalindrom(char num[]){
    // verifica se é um palindromo
    int last_position = (sizeof(num)/sizeof(char)) - 1;
    for(int i = 0; i < (sizeof(num)/sizeof(char)); i++){
        if(num[last_position] != num[i]){
            printf("\nIs not a palindrom");
            return 0;
        }
        last_position--;
    }
    printf("\nIs a palindrom");
    return 0;
}

void sumPrimeNumber(){
    // soma numeros primos abaixo de 2mi
    int sum = 0;
    for(int i = 0; i < 20; i++){
        sum += isPrime(i);
    }
    printf("\nSOMA: %d", sum);
}


void printPiramid(int limit){
    //printa numeros
    for(int i = 1; i <= limit; i++){
        for(int t = 1; t <= i; t++){
            printf("%d", t);
        }printf("\n");
    }
}


void solveOperations(){
    float num1, num2;
    int option;
    printf("Conforme o menu, escolha a operacao:\n");
    printf("1) adicao\n");
    printf("2) subtracao\n");
    printf("3) multiplicacao\n");
    printf("4) divisao\n");
    printf("Opcao >>> ");
    scanf("%d", &option);
    printf("Informe o num1 e num2: ");
    scanf("%f  %f: ", &num1, &num2);
    switch(option){
    case 1:
        printf("%.0f", num1 + num2);
        break;
    case 2:
        printf("%.0f", num1 - num2);
        break;
    case 3:
        printf("%.0f", num1 * num2);
        break;
    case 4:
        printf("%.2f", num1 / num2);
        break;
    default:
        printf("%f %f", num1, num2);
    }

}

void main(){
    isPrime(6);
    char vet[] = {'1', '2', '3', '1'};
    isPalindrom(vet);
    printf("\n");
    sumPrimeNumber();
    solveOperations();

}
