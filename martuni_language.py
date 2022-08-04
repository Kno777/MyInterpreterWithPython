"""
This is my interpretar Logic Modul
Do you need run my Martuni language. 
Open your terminal and write this command ` ./start_martuni.m3
"""

"""
mka -> int
gya -> double 
txt -> string
tpa -> print
ete -> if
eli -> else
"""

"""
Arithmetic Operation Support
    > , < , ==
    gum -> +
    han -> -
    baz -> *
    rbj -> /
    baj -> //
"""


class MVariable:
    """This is my Variable Class
    """
    mka = dict()
    gya = dict()
    txt = dict()
    tpa = dict()

class MMaths:
    """This is my Arithmetic Logic Class"""
    gumarum = dict()
    hanum = dict()
    patkum = dict()
    realbajanum = dict()
    bajanum = dict()
    
    def get_sum_result(self, *args, **kwargs):
        """This function retured numbers sum"""
        summer = 0
        for val in args:
            summer += val
        key = [x for x in self.gumarum]
        key = ''.join(key)
        self.gumarum[key] = summer
        return self.gumarum
    
    def get_sub_result(self, *args, **kwargs):
        """This function retured numbers sub"""
        subber = []
        for val in args:
            subber.append(val)
        sub = [subber[x] - subber[x-1] for x in range(len(subber))]
        key = [x for x in self.hanum]
        key = ''.join(key)
        self.hanum[key] = sub[0]
        return self.hanum
    
    def get_mul_result(self, *args, **kwargs):
        """This function retured numbers mul"""
        mul = 1
        for val in args:
            mul *= val
        key = [x for x in self.patkum]
        key = ''.join(key)
        self.patkum[key] = mul
        return self.patkum
    
    def get_real_div_result(self, *args, **kwargs):
        """This function retured numbers real div"""
        rdiv = []
        for val in args:
            rdiv.append(val)
        try:
            div = [rdiv[x] / rdiv[x-1] for x in range(len(rdiv))]
            key = [x for x in self.realbajanum]
            key = ''.join(key)
            self.realbajanum[key] = div[0]
            return self.realbajanum
        except ZeroDivisionError:
            print("Too ayyy cuylik qez dbrocum chen asel vor 0 tvi chen bajnum...")
            exit(0)
           
    
    def get_div_result(self, *args, **kwargs):
        """This function retured numbers div"""
        rdiv = []
        for val in args:
            rdiv.append(val)
        try:
            div = [rdiv[x] // rdiv[x-1] for x in range(len(rdiv))]
            key = [x for x in self.bajanum]
            key = ''.join(key)
            self.bajanum[key] = div[0]
            return self.bajanum
        except ZeroDivisionError:
            print("Too ayyy cuylik qez dbrocum chen asel vor 0 tvi chen bajnum...")
            exit(0)
    

class MTypeCheck:
    """This is my Syntax and Type chack class
    """
    _syntax = ('mka', 'gya', '=', ';', ' ', 'tpa', 'ete', 'eli', '>>', 'txt', '"', 'then')
    _syntax_for_math = ('gum', 'han', 'baz', 'rbj', 'baj')
    _error = "Gyda edamal sxla kenes du"
    _error_for_dot = "Ehhh mi moraci gyada et ander -> ';' "
    _error_for_equal = "Gydaa che cragarvorumy qezi hamar che '=' <- mi moraci dir!"
    _error_for_variable = "Kartol eli popoxakani anund ov pidi horini ay ta..."
    _error_for_tpa = "Nevayncucir gyaaa '>>' <- arc dra ches kara tpes..."
    _error_for_undifinde_var = "Harajin angam kdenam edmal popoxakan gyaaa chi krna lini..."
    _error_for_str_kavichka = "Laa dee ehh edmal ban mi ara txt greluc ' ->""<- ' anpayman dir..."
    _error_for_gumarum_plus = "Aytaa gumarum es uzum anes et ander nshany dir '+' vyyy"
    _error_for_hanum_minus = "Aytaa hanum es uzum anes et ander nshany dir '-' vyyy"
    _error_for_real_bajanum = "Aytaa real bajanum es uzum anes et ander nshany dir '/' vyyy"
    _error_for_bajanum = "Aytaa bajanum es uzum anes et ander nshany dir '//' vyyy"
    _error_for_patkum_baz = "Aytaa bazmapatkum es uzum anes et ander nshany dir '*' vyyy"
    _error_for_maths = "Ayy mard hogna es arden gorcoxutyun es uzum anes es anter menak dir eli ('+')"
    
    var = MVariable()
    mat = MMaths()
    
    def chack_full(self):
        
        f = open('compile.txt')
        for char in f.readlines():
            char = char.replace("\n", "")
            dot = [x for x in char]
            
            if char[:3] == self._syntax_for_math[0]:
                gm = [x for x in char]
                gum_key = ''
                one_key = ''
                two_key = ''
                one_key_for_mka = False
                one_key_for_gya = False
                
                two_key_for_mka = False
                two_key_for_gya = False
                
                if gm.count('+') == 1:
                    for val in gm[4:]:
                        if val == '=':
                            break
                        gum_key += val
                    gum_key = gum_key.rstrip(' ')
                    self.mat.gumarum.setdefault(gum_key, None)

                    for val in gm[8:]:
                        if val == '+':
                            break
                        one_key += val
                    one_key = one_key.rstrip(' ')

                    for val in gm[12:]:
                        if val == ';':
                            break
                        two_key += val
                    two_key = two_key.rstrip(' ')
                    
                    
                    if one_key in self.var.mka.keys():
                        one_key_for_mka = True
                        
                    elif one_key in self.var.gya.keys():
                        one_key_for_gya = True
            
                    if two_key in self.var.mka.keys():
                        two_key_for_mka = True
                        
                    elif two_key in self.var.gya.keys():
                        two_key_for_gya = True

                    if one_key_for_mka and one_key_for_gya:
                        o_mka = self.var.mka[one_key]
                        o_gya = self.var.gya[one_key]
                        self.mat.get_sum_result(o_mka, o_gya)
                        
                    if one_key_for_mka and two_key_for_mka:
                        o_mka = self.var.mka[one_key]
                        o_gya = self.var.mka[two_key]
                        self.mat.get_sum_result(o_mka, o_gya)
                    
                    if one_key_for_mka and two_key_for_gya:
                        o_mka = self.var.mka[one_key]
                        o_gya = self.var.gya[two_key]
                        self.mat.get_sum_result(o_mka, o_gya)
                    
                    if one_key_for_gya and two_key_for_mka:
                        o_mka = self.var.gya[one_key]
                        o_gya = self.var.mka[two_key]
                        self.mat.get_sum_result(o_mka, o_gya)
                    
                    if one_key_for_gya and two_key_for_gya:
                        o_mka = self.var.gya[one_key]
                        o_gya = self.var.gya[two_key]
                        self.mat.get_sum_result(o_mka, o_gya)
                    
                    if two_key_for_mka and two_key_for_gya:
                        o_mka = self.var.gya[one_key]
                        o_gya = self.var.gya[two_key]
                        self.mat.get_sum_result(o_mka, o_gya)
                            
                elif gm.count('+') == 0:
                    print(self._error_for_gumarum_plus)
                elif gm.count('+') > 1:
                    print("Ehhh du ski chgites vor mihat '+'-es nshanov en gumarum anum ay ta?")
                else:
                    pass
                
                    
            if char[:3] == self._syntax_for_math[1]:
                hn = [x for x in char]
                han_key = ''
                hone_key = ''
                htwo_key = ''
                hone_key_for_mka = False
                hone_key_for_gya = False
                
                htwo_key_for_mka = False
                htwo_key_for_gya = False
                
                if hn.count('-') == 1:
                    for val in hn[4:]:
                        if val == '=':
                            break
                        han_key += val
                    han_key = han_key.rstrip(' ')
                    self.mat.hanum.setdefault(han_key, None)

                    for val in hn[8:]:
                        if val == '-':
                            break
                        hone_key += val
                    hone_key = hone_key.rstrip(' ')

                    for val in hn[12:]:
                        if val == ';':
                            break
                        htwo_key += val
                    htwo_key = htwo_key.rstrip(' ')
                    
                    
                    if hone_key in self.var.mka.keys():
                        hone_key_for_mka = True
                        
                    elif hone_key in self.var.gya.keys():
                        hone_key_for_gya = True
            
                    if htwo_key in self.var.mka.keys():
                        htwo_key_for_mka = True
                        
                    elif htwo_key in self.var.gya.keys():
                        htwo_key_for_gya = True

                    if hone_key_for_mka and hone_key_for_gya:
                        ho_mka = self.var.mka[hone_key]
                        ho_gya = self.var.gya[hone_key]
                        self.mat.get_sub_result(ho_mka, ho_gya)
                        
                    if hone_key_for_mka and htwo_key_for_mka:
                        ho_mka = self.var.mka[hone_key]
                        ho_gya = self.var.mka[htwo_key]
                        self.mat.get_sub_result(ho_mka, ho_gya)
                    
                    if hone_key_for_mka and htwo_key_for_gya:
                        ho_mka = self.var.mka[hone_key]
                        ho_gya = self.var.gya[htwo_key]
                        self.mat.get_sub_result(ho_mka, ho_gya)
                    
                    if hone_key_for_gya and htwo_key_for_mka:
                        ho_mka = self.var.gya[hone_key]
                        ho_gya = self.var.mka[htwo_key]
                        self.mat.get_sub_result(ho_mka, ho_gya)
                    
                    if hone_key_for_gya and htwo_key_for_gya:
                        ho_mka = self.var.gya[hone_key]
                        ho_gya = self.var.gya[htwo_key]
                        self.mat.get_sub_result(ho_mka, ho_gya)
                    
                    if htwo_key_for_mka and htwo_key_for_gya:
                        ho_mka = self.var.gya[hone_key]
                        ho_gya = self.var.gya[htwo_key]
                        self.mat.get_sub_result(ho_mka, ho_gya)
                            
                elif hn.count('-') == 0:
                    print(self._error_for_hanum_minus)
                elif hn.count('-') > 1:
                    print("Ehhh du ski chgites vor mihat '-'-es nshanov en gumarum anum ay ta?")
                else:
                    pass
            
            if char[:3] == self._syntax_for_math[2]:
                pt = [x for x in char]
                mul_key = ''
                mone_key = ''
                mtwo_key = ''
                mone_key_for_mka = False
                mone_key_for_gya = False
                
                mtwo_key_for_mka = False
                mtwo_key_for_gya = False
                
                if pt.count('*') == 1:
                    for val in pt[4:]:
                        if val == '=':
                            break
                        mul_key += val
                    mul_key = mul_key.rstrip(' ')
                    self.mat.patkum.setdefault(mul_key, None)

                    for val in pt[8:]:
                        if val == '*':
                            break
                        mone_key += val
                    mone_key = mone_key.rstrip(' ')

                    for val in pt[12:]:
                        if val == ';':
                            break
                        mtwo_key += val
                    mtwo_key = mtwo_key.rstrip(' ')
                    
                    
                    if mone_key in self.var.mka.keys():
                        mone_key_for_mka = True
                        
                    elif mone_key in self.var.gya.keys():
                        mone_key_for_gya = True
            
                    if mtwo_key in self.var.mka.keys():
                        mtwo_key_for_mka = True
                        
                    elif mtwo_key in self.var.gya.keys():
                        mtwo_key_for_gya = True

                    if mone_key_for_mka and mone_key_for_gya:
                        mo_mka = self.var.mka[mone_key]
                        mo_gya = self.var.gya[mone_key]
                        self.mat.get_mul_result(mo_mka, mo_gya)
                        
                    if mone_key_for_mka and mtwo_key_for_mka:
                        mo_mka = self.var.mka[mone_key]
                        mo_gya = self.var.mka[mtwo_key]
                        self.mat.get_mul_result(mo_mka, mo_gya)
                    
                    if mone_key_for_mka and mtwo_key_for_gya:
                        mo_mka = self.var.mka[mone_key]
                        mo_gya = self.var.gya[mtwo_key]
                        self.mat.get_mul_result(mo_mka, mo_gya)
                    
                    if mone_key_for_gya and mtwo_key_for_mka:
                        mo_mka = self.var.gya[mone_key]
                        mo_gya = self.var.mka[mtwo_key]
                        self.mat.get_mul_result(mo_mka, mo_gya)
                    
                    if mone_key_for_gya and mtwo_key_for_gya:
                        mo_mka = self.var.gya[mone_key]
                        mo_gya = self.var.gya[mtwo_key]
                        self.mat.get_mul_result(mo_mka, mo_gya)
                    
                    if mtwo_key_for_mka and mtwo_key_for_gya:
                        mo_mka = self.var.gya[mone_key]
                        mo_gya = self.var.gya[mtwo_key]
                        self.mat.get_mul_result(mo_mka, mo_gya)
                            
                elif pt.count('*') == 0:
                    print(self._error_for_patkum_baz)
                elif pt.count('*') > 1:
                    print("Ehhh du ski chgites vor mihat '*'-es nshanov en gumarum anum ay ta?")
                else:
                    pass
                
            if char[:3] == self._syntax_for_math[3]:
                rb = [x for x in char]
                rbj_key = ''
                rone_key = ''
                rtwo_key = ''
                rone_key_for_mka = False
                rone_key_for_gya = False
                
                rtwo_key_for_mka = False
                rtwo_key_for_gya = False
                
                if rb.count('/') == 1:
                    for val in rb[4:]:
                        if val == '=':
                            break
                        rbj_key += val
                    rbj_key = rbj_key.rstrip(' ')
                    self.mat.realbajanum.setdefault(rbj_key, None)

                    for val in rb[8:]:
                        if val == '/':
                            break
                        rone_key += val
                    rone_key = rone_key.rstrip(' ')

                    for val in rb[12:]:
                        if val == ';':
                            break
                        rtwo_key += val
                    rtwo_key = rtwo_key.rstrip(' ')
                    
                    if rone_key in self.var.mka.keys():
                        rone_key_for_mka = True
                        
                    elif rone_key in self.var.gya.keys():
                        rone_key_for_gya = True
            
                    if rtwo_key in self.var.mka.keys():
                        rtwo_key_for_mka = True
                        
                    elif rtwo_key in self.var.gya.keys():
                        rtwo_key_for_gya = True

                    if rone_key_for_mka and rone_key_for_gya:
                        ro_mka = self.var.mka[rone_key]
                        ro_gya = self.var.gya[rone_key]
                        self.mat.get_real_div_result(ro_mka, ro_gya)
                        
                    if rone_key_for_mka and rtwo_key_for_mka:
                        ro_mka = self.var.mka[rone_key]
                        ro_gya = self.var.mka[rtwo_key]
                        self.mat.get_real_div_result(ro_mka, ro_gya)
                        
                    if rone_key_for_mka and rtwo_key_for_gya:
                        ro_mka = self.var.mka[rone_key]
                        ro_gya = self.var.gya[rtwo_key]
                        self.mat.get_real_div_result(ro_mka, ro_gya)
                    
                    if rone_key_for_gya and rtwo_key_for_mka:
                        ro_mka = self.var.gya[rone_key]
                        ro_gya = self.var.mka[rtwo_key]
                        self.mat.get_real_div_result(ro_mka, ro_gya)
                    
                    if rone_key_for_gya and rtwo_key_for_gya:
                        ro_mka = self.var.gya[rone_key]
                        ro_gya = self.var.gya[rtwo_key]
                        self.mat.get_real_div_result(ro_mka, ro_gya)
                    
                    if rtwo_key_for_mka and rtwo_key_for_gya:
                        ro_mka = self.var.gya[rone_key]
                        ro_gya = self.var.gya[rtwo_key]
                        self.mat.get_real_div_result(ro_mka, ro_gya)
                            
                elif rb.count('/') == 0:
                    print(self._error_for_real_bajanum)
                elif rb.count('/') > 1:
                    print("Ehhh du ski chgites vor mihat '/'-es nshanov en gumarum anum ay ta?")
                else:
                    pass
            
            
            if char[:3] == self._syntax_for_math[4]:
                baj = [x for x in char]
                baj_key = ''
                bone_key = ''
                btwo_key = ''
                bone_key_for_mka = False
                bone_key_for_gya = False
                
                btwo_key_for_mka = False
                btwo_key_for_gya = False
                
                if baj.count('/') == 2:
                    for val in baj[4:]:
                        if val == '=':
                            break
                        baj_key += val
                    baj_key = baj_key.rstrip(' ')
                    self.mat.bajanum.setdefault(baj_key, None)

                    for val in baj[8:]:
                        if val == '/':
                            break
                        bone_key += val
                    bone_key = bone_key.rstrip(' ')
                    
                    for val in baj[13:]:
                        if val == ';':
                            break
                        btwo_key += val
                    btwo_key = btwo_key.rstrip(' ')
                    
                    if bone_key in self.var.mka.keys():
                        bone_key_for_mka = True
                        
                    elif bone_key in self.var.gya.keys():
                        bone_key_for_gya = True
            
                    if btwo_key in self.var.mka.keys():
                        btwo_key_for_mka = True
                        
                    elif btwo_key in self.var.gya.keys():
                        btwo_key_for_gya = True

                    if bone_key_for_mka and bone_key_for_gya:
                        bo_mka = self.var.mka[bone_key]
                        bo_gya = self.var.gya[bone_key]
                        self.mat.get_div_result(bo_mka, bo_gya)
                        
                    if bone_key_for_mka and btwo_key_for_mka:
                        bo_mka = self.var.mka[bone_key]
                        bo_gya = self.var.mka[btwo_key]
                        self.mat.get_div_result(bo_mka, bo_gya)
                    
                    if bone_key_for_mka and btwo_key_for_gya:
                        bo_mka = self.var.mka[bone_key]
                        bo_gya = self.var.gya[btwo_key]
                        self.mat.get_div_result(bo_mka, bo_gya)
                    
                    if bone_key_for_gya and btwo_key_for_mka:
                        bo_mka = self.var.gya[bone_key]
                        bo_gya = self.var.mka[btwo_key]
                        self.mat.get_div_result(bo_mka, bo_gya)
                    
                    if bone_key_for_gya and btwo_key_for_gya:
                        bo_mka = self.var.gya[bone_key]
                        bo_gya = self.var.gya[btwo_key]
                        self.mat.get_div_result(bo_mka, bo_gya)
                    
                    if btwo_key_for_mka and btwo_key_for_gya:
                        bo_mka = self.var.gya[bone_key]
                        bo_gya = self.var.gya[btwo_key]
                        self.mat.get_div_result(bo_mka, bo_gya)
                            
                elif gm.count('/') == 0:
                    print(self._error_for_bajanum)
                elif gm.count('/') > 2:
                    print("Ehhh du ski chgites vor mihat '+'-es nshanov en gumarum anum ay ta?")
                else:
                    pass
            
            
            if char[:3] == self._syntax[5]:
                tp = [x for x in char]
                keys = tp
                new_key = ''
                for val in keys[7:]:
                    new_key += val
                new_key = new_key.rstrip(';')
                
                if tp.count('>') == 2:
                    if new_key in self.var.gya.keys():
                        self.var.tpa.setdefault(new_key, self.var.gya[new_key])
                        print(self.var.tpa[new_key])
                    elif new_key in self.var.mka.keys():
                        self.var.tpa.setdefault(new_key, self.var.mka[new_key])
                        print(self.var.tpa[new_key])
                    elif new_key in self.var.txt.keys():
                        self.var.tpa.setdefault(new_key, self.var.txt[new_key])
                        print(self.var.tpa[new_key])
                    elif new_key in self.mat.gumarum.keys():
                        self.var.tpa.setdefault(new_key, self.mat.gumarum[new_key])
                        print(self.var.tpa[new_key])
                    elif new_key in self.mat.hanum.keys():
                        self.var.tpa.setdefault(new_key, self.mat.hanum[new_key])
                        print(self.var.tpa[new_key])
                    elif new_key in self.mat.patkum.keys():
                        self.var.tpa.setdefault(new_key, self.mat.patkum[new_key])
                        print(self.var.tpa[new_key])
                    elif new_key in self.mat.realbajanum.keys():
                        self.var.tpa.setdefault(new_key, self.mat.realbajanum[new_key])
                        print(self.var.tpa[new_key])
                    elif new_key in self.mat.bajanum.keys():
                        self.var.tpa.setdefault(new_key, self.mat.bajanum[new_key])
                        print(self.var.tpa[new_key])
                    else:
                        print(self._error_for_undifinde_var)
                else:
                    print(self._error_for_tpa)
            else:
                if self._syntax[3] not in dot:
                    print(self._error_for_dot)
                
                if self._syntax[6:8]:
                    pass
                elif self._syntax[2] not in dot:
                    print(self._error_for_equal)
                
                if dot[4] == ' ' or dot[4] == "=":
                    print(self._error_for_variable)
            
            if char[:3] == self._syntax[6]: # ete
                tiv = [x for x in char if x.isdigit()]
                arth = [x for x in char]
                x = ''.join(arth)
                i = 0
                exp = ''
                bools = False
                while i != x.index(';'):
                    if s:=self.get_arithmethic_symbol(x[i]):
                        exp = s
                    i += 1
                
                t1 = int(tiv[0])
                t2 = int(tiv[1])
                
                if self.get_my_sym(exp) == '<':
                    if t1 < t2:
                        bools = True
                elif self.get_my_sym(exp) == '>':
                    if t1 > t2:
                        bools = True
                elif self.get_my_sym(exp) == '=':
                    if t1 == t2:
                        bools = True
                        
                if bools:
                    k = char.index("tpa")
                    nor_key = ''
                    d = char.rindex('>')
                    while d < char.rindex(';'):
                        nor_key += char[d]
                        d += 1
                    nor_key = nor_key.strip(' >')
                    
                    if nor_key in self.var.gya.keys():
                        self.var.tpa.setdefault(nor_key, self.var.gya[nor_key])
                        print(self.var.tpa[nor_key])
                    elif nor_key in self.var.mka.keys():
                        self.var.tpa.setdefault(nor_key, self.var.mka[nor_key])
                        print(self.var.tpa[nor_key])
                    elif nor_key in self.var.txt.keys():
                        self.var.tpa.setdefault(nor_key, self.var.txt[nor_key])
                        print(self.var.tpa[nor_key])
                
            if char[:3] in self._syntax[0]: # int
                mk = [x for x in char]
                value = ''
                key = ''
                for val in mk[8:]:
                    if val.isalnum():
                        value += val
                        
                for val in mk[4:]:
                    if val == '=':
                        break
                    key += val
                key = key.rstrip(' ')
                self.var.mka.setdefault(key, int(value))
            
            if char[:3] == self._syntax[1]: # double
                gy = [x for x in char]
                value = ''
                key = ''
                for val in gy[8:]:
                    if val.isalnum() or val == '.':
                        value += val
                        
                for val in gy[4:]:
                    if val == '=':
                        break
                    key += val
                    key = key.rstrip(' ')
                self.var.gya.setdefault(key, float(value))
            
            
            if char[:3] == self._syntax[9]: # string
                tx = [x for x in char]
                line = ''
                key = ''
                if tx.count('"') == 2:
                    for val in tx[9:]:
                        if val.isalpha():
                            line += val
                            
                    for val in tx[4:]:
                        if val == '=':
                            break
                        key += val
                    key = key.rstrip(' ')
                    self.var.txt.setdefault(key, str(line))
                else:
                    print(self._error_for_str_kavichka)
            
            
            if char[:3] not in self._syntax[:2] and \
                char[:3] not in self._syntax[5:7] and \
                char[:3] not in self._syntax[9:10] and \
                char[:3] not in self._syntax_for_math:
                err = ''
                for ch in char:
                    if ch == " ":
                        break
                    err += ch
                print(self._error + " " 
                                  + "Martuna lezun chi ajakcum edmal popoxakan ->" 
                                  + " " + err)
        
        f.close()
    
    def get_arithmethic_symbol(self, sym:str):
        """This function chacked my smybol and return it"""
        if sym == '>' or sym == '<' or sym == '=':
            sym = sym
            return sym
        return False
    
    def get_my_sym(self, s):
        """This function return my smybol"""
        return s
