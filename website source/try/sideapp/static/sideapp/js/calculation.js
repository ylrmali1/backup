
var height = document.querySelector("#height");
var weight = document.querySelector("#weight");
var bke = document.querySelector("#bke");
var result = document.querySelector(".result1");
var calculationBtn = document.querySelector(".form-btn");
var clearBtn = document.querySelector(".clear-btn");


weight.addEventListener("keypress",(event)=>{
    if (event.key === "Enter"){
        var boy = parseInt(height.value)*parseInt(height.value);
        var kilo = parseInt(weight.value);
        var total = parseFloat(kilo/boy)*10000;
        console.log(total);
        bke.value = total;
        if (parseInt(height.value)<2){
            result.textContent = "Boyunuzu hatalı girdiniz.Lütfen boyunuzu santimetre cinsinden giriniz! Örneğin 175";
        }
        else{
            if (total<18.49){
                result.textContent = "İdeal kilonun altındasın!! Bizimle iletişime geçip sağlıklı kilo alabilirsin. 0505 409 58 35";
            }
            else if(total>=18.5 && total<=24.99){
                result.textContent = "İdeal kilodasınız. Formunuzu korumak içini bizimle iletişime geçiniz. 0505 409 58 35";
            }
            else if(total>=25 && total<=29.99){
                result.textContent = "İdeal kilonun üzerindesiniz. İdeal kiloya ulaşmak için bizimle iletişime geçiniz. 0505 409 58 35";
            }
            else if(total>=30){
                result.textContent = "İdeal kilonun çok üzerindesiniz. Sağlıklı şekilde kilo vermek için bizimle iletişime geçiniz. 0505 409 58 35";
            }
            else{
                result.textContent = "Hatalı değer girdiniz!";
            }
        }
        
        event.preventDefault();

        calculationBtn.click();

    }

});

calculationBtn.addEventListener('click',()=>{
    var boy = parseInt(height.value)*parseInt(height.value);
    var kilo = parseInt(weight.value);
    var total = parseFloat(kilo/boy)*10000;
    console.log(total);
    bke.value = total;
    if (parseInt(height.value)<2){
        result.textContent = "Boyunuzu hatalı girdiniz.Lütfen boyunuzu santimetre cinsinden giriniz! Örneğin 175";
    }
    else{
        if (total<18.49){
            result.textContent = "İdeal kilonun altındasın!! Bizimle iletişime geçip sağlıklı kilo alabilirsin. 0505 409 58 35";
        }
        else if(total>=18.5 && total<=24.99){
            result.textContent = "İdeal kilodasınız. Formunuzu korumak içini bizimle iletişime geçiniz. 0505 409 58 35";
        }
        else if(total>=25 && total<=29.99){
            result.textContent = "İdeal kilonun üzerindesiniz. İdeal kiloya ulaşmak için bizimle iletişime geçiniz. 0505 409 58 35";
        }
        else if(total>=30){
            result.textContent = "İdeal kilonun çok üzerindesiniz. Sağlıklı şekilde kilo vermek için bizimle iletişime geçiniz. 0505 409 58 35";
        }
        else{
            result.textContent = "Hatalı değer girdiniz!";
        }
    }
    
});

clearBtn.addEventListener('click',()=>{
    result.textContent = "";
    bke.value = "";
    height.value ="";
    weight.value ="";
})

