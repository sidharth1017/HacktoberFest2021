#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<windows.h>


#define r 40
#define c 20

void SnakeCreate();
void print();
void reset();
void food();
int getkey();
void movement();
void RemoveTail();
void Gameover();

int i,j,field[c][r],x,y,grow,head,tail,game,frog,a,b,get,dir,score,HighScore,speed;

FILE *f;

void SnakeCreate(){
    f=fopen("HighScore.txt","r");
    fscanf(f,"%d",&HighScore);
    fclose(f);
    for(i=0;i<=c;i++){
        for(j=0;j<=r;j++){
            field[i][j]=0;
        }
    }
    x = c/2;    // x which take a place for snake's head.
    y = r/2;    // y which take a place for snake's tail.
    grow = y;   // grow which grow the size of tail.
    head = 5;
    tail = 1;
    game = 0;
    frog = 0;
    dir = 'd';
    score = 0;
    speed = 99;

    for(i=0;i<head;i++){
        grow++;
        field[x][grow-head] = i+1;
    }
}

void print(){

    printf("\t\t\t\t");
    printf("Current Score  :-  %d     HIGHSCORE  :-  %d",score,HighScore);
    printf("\n");
    printf("\t\t\t\t");
    for(i=0;i<=r+1;i++){
        if(i == 0){
            printf("%c",201);
        }else if(i == r+1){
            printf("%c",187);
        }else{
            printf("%c",205);
        }
    }
    printf("\n");

    for(i=0;i<c;i++)
    {
        printf("\t\t\t\t");
        printf("%c",186);
        for(j=0;j<r;j++){
            if(field[i][j] == 0)
                printf(" ");

            if(field[i][j]>0 && field[i][j]!=head)
                printf("%c",176);

            if(field[i][j]==head)
                printf("%c",178);

            if(field[i][j] == -1)
                printf("%c",153);

            if(j == r-1)
                printf("%c\n",186);

        }
    }

    printf("\t\t\t\t");
    for(i=0;i<=r+1;i++){
        if(i == 0){
            printf("%c",200);
        }else if(i == r+1){
            printf("%c",188);
        }else{
            printf("%c",205);
        }
    }
    printf("\n");
    printf("\t\t\t\t");
    for(i=0;i<=r+1;i++){
        if(i == 0){
            printf("%c",200);
        }else if(i == r+1){
            printf("%c",188);
        }else{
            printf("%c",205);
        }
    }
}


void reset(){

   HANDLE sOut;
   COORD Position;
   sOut = GetStdHandle(STD_OUTPUT_HANDLE);
   Position.X = 0;
   Position.Y = 0;
   SetConsoleCursorPosition(sOut,Position);
}

void food(){
    srand(time(0));
    a = 1 + rand() % 18;
    b = 1 + rand() % 38;
    if(frog == 0 && field[a][b] == 0){
        field[a][b] = -1;
        frog = 1;
        if(speed > 10 && score !=0)
            speed = speed -4;
    }
}

int getkey(){
    if(_kbhit()){
        return _getch();
    }else{
        return -1;
    }
}

void movement(){
    get = getkey();
    get = tolower(get);
    if(((get=='d' ||get=='a')||(get=='w' ||get=='s'))&&(abs(dir-get)>5))
        dir=get;
    if(dir == 'd'){
        y++;
        if(field[x][y] != 0 && field[x][y] != -1){
            system("color 4");
            Gameover();
        }
        if(y == r){
            system("color 4");
            Gameover();
        }
        if(field[x][y]==-1){
            frog = 0;
            score+=5;
            tail -= 2;
        }
        head++;
        field[x][y] = head;
    }
    if(dir == 'a'){
        y--;
        if(field[x][y] != 0 && field[x][y] != -1){
            system("color 4");
            Gameover();
        }
        if(y == -1){
            system("color 4");
            Gameover();
        }
        if(field[x][y]==-1){
            frog = 0;
            score+=5;
            tail -= 3;
        }
        head++;
        field[x][y] = head;
    }
    if(dir == 'w'){
        x--;
        if(field[x][y] != 0 && field[x][y] != -1){
            system("color 4");
            Gameover();
        }
        if(x == -1){
            system("color 4");
            Gameover();
        }
        if(field[x][y]==-1){
            frog = 0;
            score+=5;
            tail -= 3;
        }
        head++;
        field[x][y] = head;
    }
    if(dir == 's'){
        x++;
        if(field[x][y] != 0 && field[x][y] != -1){
            system("color 4");
            Gameover();
        }
        if(x==c){
            system("color 4");
            Gameover();
        }
        if(field[x][y]==-1){
            frog = 0;
            score+=5;
            tail -= 3;
        }
        head++;
        field[x][y] = head;
    }
}

void RemoveTail(){
    for(i=0;i<c;i++){
        for(j=0;j<r;j++){
            if(field[i][j]==tail){
                field[i][j] = 0;
            }
        }
    }
    tail++;
}

void Gameover(){
    printf("\a");
    Sleep(1500);
    system("cls");
    if(score>HighScore){
        printf("\n\n\tTHE NEW HIGHSCORE IS  :-  %d\n\n",score);
        system("pause");
        f=fopen("HighScore.txt","w");
        fprintf(f,"%d",score);
        fclose(f);
    }
    system("cls");
    printf("\n\n\n\n");
    printf("\tGAME OVER !!!!!!\n");
    printf("\tYOUR SCORE = %d",score);
    printf("\t\n\nPress ENTER to play again or ESC to exit...");
    while(1){
        get=getkey();
        if(get == 13){
            game=0;
            SnakeCreate();
            break;
        }else if(get == 27){
            game = 1;
            break;
        }
    }
    system("cls");
}

void main(){
    SnakeCreate();
    while(game == 0){
        print();
        reset();
        system("color 9");
        food();
        movement();
        RemoveTail();
        Sleep(speed);
    }
}
