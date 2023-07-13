#include <iostream>
#include <fstream>
#include <string>

int partOne(std::string file)
{
    std::ifstream infile(file);
    std::string line1, line2;
    while (std::getline(infile, line1))
    {
        std::ifstream infile2(file);
        while (std::getline(infile2, line2))
        {
            int num1 = std::stoi(line1);
            int num2 = std::stoi(line2);
            if (line1 != line2)
            {
                int sum = num1 + num2;
                if (sum == 2020)
                {
                    return num1 * num2;
                }
            }
        }
    }
    return 0;
}

int partTwo(std::string file)
{
    std::ifstream infile(file);
    std::string line1, line2, line3;
    while (std::getline(infile, line1))
    {
        std::ifstream infile2(file);
        while (std::getline(infile2, line2))
        {
            std::ifstream infile3(file);
            while (std::getline(infile3, line3))
            {
                int num1 = std::stoi(line1);
                int num2 = std::stoi(line2);
                int num3 = std::stoi(line3);
                if (line1 != line2 && line1 != line3 && line2 != line3)
                {
                    int sum = num1 + num2 + num3;
                    if (sum == 2020)
                    {
                        return num1 * num2 * num3;
                    }
                }
            }
        }
    }
    return 0;
}

int main()
{
    std::string file = "input.txt";
    int partOneResult = partOne(file);
    int partTwoResult = partTwo(file);
    std::cout << "Part One: " << partOneResult << std::endl;
    std::cout << "Part Two: " << partTwoResult << std::endl;
    return 0;
}
