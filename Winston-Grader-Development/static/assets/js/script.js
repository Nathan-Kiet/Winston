function test(){
    const span = document.getElementById('GPAoutput');
    const percArray = [
        document.getElementById("num1").value, document.getElementById("num2").value, document.getElementById("num3").value, document.getElementById("num4").value, document.getElementById("num5").value, document.getElementById("num6").value, document.getElementById("num7").value, document.getElementById("num8").value, document.getElementById("num9").value
    ]
    const gpaNum = [];
    let arrayLength = percArray.length;
    const average = array => array.reduce((a, b) => a + b) / array.length;
    for (let i = 0; i < arrayLength; i++){
        if (percArray[i]>92){// A/A+
            gpaNum[i] = 4.0
        }else if(percArray[i]>89){// A-
            gpaNum[i] = 3.7
        }else if(percArray[i]>86){// B+
            gpaNum[i] = 3.3
        }else if(percArray[i]>82){// B
            gpaNum[i] = 3.0
        }else if(percArray[i]>79){// B-
            gpaNum[i] = 2.7
        }else if(percArray[i]>76){// C+
            gpaNum[i] = 2.3
        }else if(percArray[i]>72){// C
            gpaNum[i] = 2.0
        }else if(percArray[i]>69){// C-
            gpaNum[i] = 1.7
        }else if(percArray[i]>66){// D+
            gpaNum[i] = 1.3
        }else if(percArray[i]>65){// D
            gpaNum[i] = 1.0
        }else if(percArray[i]<65){// E/F
            gpaNum[i] = 0.0
        }
    }
    span.textContent = Math.round(average(gpaNum) * 10) / 10
}