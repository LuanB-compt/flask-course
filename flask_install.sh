#!/bin/bash

Help()
{
    echo "This script install the Flask framework to your conda env" 
    echo
    echo "Syntax: python_install.sh [-env|h]"
    echo "Options:"
    echo "-h     Help function"
    echo "-env   Select the conda environment."
    echo
    echo "EXAMPLE:"
    echo "bash python_install.sh -h      (Help function)"
    echo "bash python_install.sh -env [environment]"
    echo
}

while getops "he:" flag
do
    case "${flag}" in
        h) 
        Help
        exit;;
        env) environment=${OPTARG};;
        \?)
        echo "Error: invalid option"
        exit;;
    esac
done

# Execute the installation
echo "Installing the Flask in $environment env"
echo "conda activate $environment"
conda env list
which pip