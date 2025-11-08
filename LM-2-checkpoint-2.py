import string

def calculate_frequency(ciphertext, cipher_name):
    processed_text = "".join(filter(str.isalpha, ciphertext)).upper()
    total_letters = len(processed_text)

    freq_map = {}
    for letter in string.ascii_uppercase:
        freq_map[letter] = processed_text.count(letter)

    sorted_freq = sorted(
        freq_map.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print(f"Frequency Analysis for {cipher_name}")
    print(f"Total Letters: {total_letters}") 
    print("-------------------------------------------------")
    print("Rank | Cipher Letter | Count | Percentage | Likely Plaintext (E, T, A...)")
    print("-------------------------------------------------")


    english_rank = ["E", "T", "A", "O", "I", "N", "S", "H", "R", "D", "L", "U"] 

    for rank, (char, count) in enumerate(sorted_freq):
        if count > 0:
            percentage = (count / total_letters) * 100

            guess = english_rank[rank] if rank < len(english_rank) else '?'

            print(f"{rank+1:4} | {char:13} | {count:5} | {percentage:10.2f}% | {guess}")


cipher1 = "af p xpkcaqvnpk pfg, af ipqe qpri, gauuikifc tpw, ceiri udvk tiki afgarxifrphni cd eao--wvmd popkwn, hiqpvri du ear jvaql vfgikrcpfgafm du cei xkafqaxnir du xrwqedearcdkw pfg du ear aopmafpcasi xkdhafmr afcd fit pkipr. ac tpr qdoudkcafm cd Ifdt cepc au pfwceafm epxxifig cd ringdf eaorinu hiudki cei opceiopcaqr du cei uaing qdvng hi qdoxnicinw tdklig dvc--pfg edt rndtnw ac xkdqiigig, pfg edt odvfcpafdvr cei dhrcpqnir--ceiki tdvng pc niprc kiopaf dfi mddg oafg cepc tdvng qdfcafvi cei kiripkqe"


cipher2 = "aceah toz puvg vcdl omj puvg yudqecov, omj loj auum klu thmjuv hs klu zlcvu shv zcbkg guovz, upuv zcmdu Icz vuwovroaeu jczoyyuovomdu omj qmubyudkuj vukqvm. klu vcdluz lu loj avhqnlk aodr svhw Icz kvopuez loj mht audhwu o ehdoe eunumj, omj ck toz yhyqeoveg auecupuj, tlokupuv klu hej sher wcnik zog, klok klu Icee ok aon umj toz sqee hs kqmmuez zkqssuj tcki kvuozqvu. omj cs klok toz mhk umhqni shv sowu, kluvu toz oezh Icz yvhehmnuj pcnhqv kh wovpue ok. kcwu thvu hm, aqk ck zuuwuj kh lopu eckkeu ussudk hm wv. aonncmz. ok mcmukg lu toz wądl klu zowu oz ok scskg. ok mcmukg-mcmu klug aunom kh doee Icw tuee-yvuzuvpuj; aqk qmdlomnuj thqej lopu auum muovuv klu wovr. kluvu tuvu zhwu klok zlhhr klucv luojz omj klhqnik klcz toz khh wqdl hs o nhhj klcmn; ck zuuwuj qmsocv klok omghmu zihqej yhzzuzz (oyyovumkeg) yuvyukqoe ghqkl oz tuee oz (vuyqkujeg) cmubloqzkcaeu tuoekl. ck tcee lopu kh au yocj shv, klug zocj. ck czm'k mokqvoe, omj kvhqaeu tcee dhwu hs ck! aqk zh sov kvhqaeu loj mhk dhwu; omj oz wv. aonncmz toz numuvhqz tckl Icz whmug, whzk yuhyeu tuvu tceecmn kh shvncpu Icw Icz hjjckcuz omj Icz nhhj shvkqmu. lu vuwocmuj hm pczckcmn kuvwz tckl Icz vueokcpuz (ubduyk, hs dhqvzu, klu zodrpceeu- aonncmzuz), omj lu loj womg juphkuj ojwcvuvz owhmn klu Ihaackz hs yhhv omj qmcwyhvkomk sowcecuz. aqk lu loj mh dehzu svcumjz, qmkce zhwu hs lcz ghqmnuv dhqzcmz aunom kh nvht qy. klu uejuzk hs kluzu, omj aceah'z sophqvcku, toz ghqmn svhjh aonncmz. tlum aceah toz mcmukg-mcmu lu ojhykuj svhjh oz lcz lucv, omj avhqnlk Icw kh ecpu ok aon umj; omj klu lhyuz hs klu zodrpceeu- aonncmzuz tuvu scmoeeg jozluj. aceah omj svhjh loyyumuj kh lopu klu zowu acvkljog, zuykuwauv 22mj. ghq loj aukkuv dhwu omj ecpu luvu, svhjh wg eoj, zocj aceah hmu jog; omj klum tu dom dueuavoku hqv acvkljog-yovkcuz dhwshvkoaeg khnukluv. ok klok kcwu svhjh toz zkcee cm Icz ktuumz, oz klu lhaackz doeeuj klu cvvuzyhmzcaeu ktumkcuz auktuum dicejlhhj omj dhwcmn hs onu ok klcvkg-klvuu"

calculate_frequency(cipher1, "Cipher-1")
calculate_frequency(cipher2, "Cipher-2")