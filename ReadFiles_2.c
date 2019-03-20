//Linux C
//LINUX/UNIX c获取某个目录下的所有文件的文件名
 
#include <stdio.h>
#include <dirent.h>
int main(int argc, char * argv[])
{
    struct dirent *ptr;    
    DIR *dir;
    dir=opendir("./file");
    printf("文件列表:\n");
    while((ptr=readdir(dir))!=NULL)
    {
 
        //跳过'.'和'..'两个目录
        if(ptr->d_name[0] == '.')
            continue;
        printf("%s\n",ptr->d_name);
    }
    closedir(dir);
    return 0;
}
