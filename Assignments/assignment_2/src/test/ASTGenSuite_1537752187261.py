#########################################################
########### Code used for Pylint to link code ###########
######    REMEMBER: Comment before submit code    #######
#########################################################

import sys
sys.path.append('../main/mp/utils')
sys.path.append('../utils')

#########################################################
######    REMEMBER: Comment before submit code    #######
#########################################################
import unittest
from TestUtils import TestAST
from AST import *
# from AntiAST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_1(self):
        input = r"""
var a: integer;
"""
        expect =str(Program([VarDecl(Id(r'a'),IntType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_2(self):
        input = r"""
var a,b: string;
"""
        expect =str(Program([VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType())]))                     
        self.assertTrue(        TestAST.test(         input,       expect,         302))

    def test_3(self):
        input = r"""
var x,y,z:integer; 
    g: string; 
    h,t: real;
"""
        expect=str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType()),VarDecl(Id(r'g'),StringType()),VarDecl(Id(r'h'),FloatType()),VarDecl(Id(r't'),FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4(self):
        input = r"""
var a:integer;
var b:string;
    f,g: real;
var t,h: string;
    p,q: boolean;
"""
        expect =str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'f'),FloatType()),VarDecl(Id(r'g'),FloatType()),VarDecl(Id(r't'),StringType()),VarDecl(Id(r'h'),StringType()),VarDecl(Id(r'p'),BoolType()),VarDecl(Id(r'q'),BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5(self):
        input = r"""
procedure foo();
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_6(self):
        input = r"""
procedure foo(a: string);
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_7(self):
        input = r"""
procedure foo(a: string; b: Real);
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),FloatType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_8(self):
        input = r"""
procedure foo(a,b,c: string);
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),StringType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_9(self):
        input = r"""
procedure foo(a,b,c: string; f,k,o: integer; g,h,t: Real);
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'f'),IntType()),VarDecl(Id(r'k'),IntType()),VarDecl(Id(r'o'),IntType()),VarDecl(Id(r'g'),FloatType()),VarDecl(Id(r'h'),FloatType()),VarDecl(Id(r't'),FloatType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10(self):
        input = r"""
function foo(): String;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_11(self):
        input = r"""
function foo(a: string): String;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType())],[],[],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_12(self):
        input = r"""
function foo(a: string; b: Real): String;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),FloatType())],[],[],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_13(self):
        input = r"""
function foo(a,b,c: string; 
    f,k,o: integer; g,h,t: Real): String;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'f'),IntType()),VarDecl(Id(r'k'),IntType()),VarDecl(Id(r'o'),IntType()),VarDecl(Id(r'g'),FloatType()),VarDecl(Id(r'h'),FloatType()),VarDecl(Id(r't'),FloatType())],[],[],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_14(self):
        input = r"""
function foo(): String;
begin
continue;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Continue()],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_15(self):
        input = r"""
function foo(): String;
begin
break;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Break()],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16(self):
        input = r"""
function foo(): String;
begin
return;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Return(None)],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_17(self):
        input = r"""
function foo(): String;
begin
return ok();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Return(CallExpr(Id(r'ok'),[]))],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_18(self):
        input = r"""
function foo(): String;
begin
return ok(1);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Return(CallExpr(Id(r'ok'),[IntLiteral(1)]))],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_19(self):
        input = r"""
function foo(): String;
begin
return ok(1,2);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Return(CallExpr(Id(r'ok'),[IntLiteral(1),IntLiteral(2)]))],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20(self):
        input = r"""
function foo(): String;
begin
return ok(1,a);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Return(CallExpr(Id(r'ok'),[IntLiteral(1),Id(r'a')]))],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21(self):
        input = r"""
function foo(): String;
begin
ok();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_22(self):
        input = r"""
function foo(): String;
begin
ok(a);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[Id(r'a')])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23(self):
        input = r"""
function foo(): String;
begin
ok(a,1);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[Id(r'a'),IntLiteral(1)])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_24(self):
        input = r"""
function foo(): String;
begin
ok(a,"1",True,falSe);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[Id(r'a'),StringLiteral(r'1'),BooleanLiteral(True),BooleanLiteral(False)])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_25(self):
        input = r"""
function foo(): String;
begin
ok("hi", foo());
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[StringLiteral(r'hi'),CallExpr(Id(r'foo'),[])])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26(self):
        input = r"""
function foo(): String;
begin
ok("hi", foo(bar(), 1));
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[StringLiteral(r'hi'),CallExpr(Id(r'foo'),[CallExpr(Id(r'bar'),[]),IntLiteral(1)])])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27(self):
        input = r"""
function foo(): String;
begin
ok(a[1]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(Id(r'a'),IntLiteral(1))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28(self):
        input = r"""
function foo(): String;
begin
ok(1[1]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(IntLiteral(1),IntLiteral(1))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29(self):
        input = r"""
function foo(): String;
begin
ok(foo()[1]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(1))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_30(self):
        input = r"""
function foo(): String;
begin
ok((foo())[1]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(1))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_31(self):
        input = r"""
function foo(): String;
begin
ok(a[b]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(Id(r'a'),Id(r'b'))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_32(self):
        input = r"""
function foo(): String;
begin
ok(a[foo()]);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[ArrayCell(Id(r'a'),CallExpr(Id(r'foo'),[]))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_33(self):
        input = r"""
function foo(): String;
begin
ok(4 and then 5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'andthen',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_34(self):
        input = r"""
function foo(): String;
begin
ok(4 or else 5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'orelse',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_35(self):
        input = r"""
function foo(): String;
begin
ok(4=5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'=',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_36(self):
        input = r"""
function foo(): String;
begin
ok(4>=5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'>=',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_37(self):
        input = r"""
function foo(): String;
begin
ok(4+5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'+',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_38(self):
        input = r"""
function foo(): String;
begin
ok(4 div 5);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'div',IntLiteral(4),IntLiteral(5))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_39(self):
        input = r"""
function foo(): String;
begin
ok(-4);
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[UnaryOp(r'-',IntLiteral(4))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_40(self):
        input = r"""
function foo(): String;
begin
ok(5 and then (-6 + "nt" * 3 or 5) div 7 >= a+b-(-f * not(-5*"abc")));
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[CallStmt(Id(r'ok'),[BinaryOp(r'andthen',IntLiteral(5),BinaryOp(r'>=',BinaryOp(r'div',BinaryOp(r'or',BinaryOp(r'+',UnaryOp(r'-',IntLiteral(6)),BinaryOp(r'*',StringLiteral(r'nt'),IntLiteral(3))),IntLiteral(5)),IntLiteral(7)),BinaryOp(r'-',BinaryOp(r'+',Id(r'a'),Id(r'b')),BinaryOp(r'*',UnaryOp(r'-',Id(r'f')),UnaryOp(r'not',BinaryOp(r'*',UnaryOp(r'-',IntLiteral(5)),StringLiteral(r'abc')))))))])],StringType())]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_41(self):
        input = r"""
procedure foo();
var a: integer;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),IntType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_42(self):
        input = r"""
procedure foo();
var a, b: integer; c: string;
    e, f, g: Boolean;
begin
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'e'),BoolType()),VarDecl(Id(r'f'),BoolType()),VarDecl(Id(r'g'),BoolType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_43(self):
        input = r"""
procedure foo();
begin
    if True then hic();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_44(self):
        input = r"""
procedure foo();
begin
    if True then hic(); else huc();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[])],[CallStmt(Id(r'huc'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_45(self):
        input = r"""
procedure foo();
begin
    if True then begin
        hic();
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_46(self):
        input = r"""
procedure foo();
begin
    if True then begin
        hic();
        break;
        continue;
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[]),Break(),Continue()],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_47(self):
        input = r"""
procedure foo();
begin
    if True then begin
        hic();
        break;
        continue;
    end else return oh();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[]),Break(),Continue()],[Return(CallExpr(Id(r'oh'),[]))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_48(self):
        input = r"""
procedure foo();
begin
    if True then begin
        hic();
        break;
        continue;
    end else begin
        return; 
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[]),Break(),Continue()],[Return(None)])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_49(self):
        input = r"""
procedure foo();
begin
    if True then begin
        hic();
        break;
        continue;
    end else begin
        oh();
        return;
        break;
        huc();
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[CallStmt(Id(r'hic'),[]),Break(),Continue()],[CallStmt(Id(r'oh'),[]),Return(None),Break(),CallStmt(Id(r'huc'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_50(self):
        input = r"""
procedure foo();
begin
    if True then begin
    end else ok();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[],[CallStmt(Id(r'ok'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51(self):
        input = r"""
procedure foo();
begin
    if True then begin
    end else begin end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[If(BooleanLiteral(True),[],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_52(self):
        input = r"""
procedure foo();
begin
    a := 1;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),IntLiteral(1))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_53(self):
        input = r"""
procedure foo();
begin
    a := 1;
    b := True;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),IntLiteral(1)),Assign(Id(r'b'),BooleanLiteral(True))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_54(self):
        input = r"""
procedure foo();
begin
    a := b := "ahihi! hic hic";
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),StringLiteral(r'ahihi! hic hic')),Assign(Id(r'b'),StringLiteral(r'ahihi! hic hic'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_55(self):
        input = r"""
procedure foo();
begin
    a[5] := "ahihi! hic hic";
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),IntLiteral(5)),StringLiteral(r'ahihi! hic hic'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_56(self):
        input = r"""
procedure foo();
begin
    foo()[5] := "ahihi! hic hic";
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(5)),StringLiteral(r'ahihi! hic hic'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_57(self):
        input = r"""
procedure foo();
begin
    a := b[4] := foo()[5] := "ahihi! hic hic";
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),StringLiteral(r'ahihi! hic hic')),Assign(ArrayCell(Id(r'b'),IntLiteral(4)),StringLiteral(r'ahihi! hic hic')),Assign(ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(5)),StringLiteral(r'ahihi! hic hic'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_58(self):
        input = r"""
procedure foo();
begin
    a[1+2] := foo(bar(), "hi", 3.4, -6.5)[4 And then trUE + FalsE];
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),BinaryOp(r'+',IntLiteral(1),IntLiteral(2))),ArrayCell(CallExpr(Id(r'foo'),[CallExpr(Id(r'bar'),[]),StringLiteral(r'hi'),FloatLiteral(3.4),UnaryOp(r'-',FloatLiteral(6.5))]),BinaryOp(r'andthen',IntLiteral(4),BinaryOp(r'+',BooleanLiteral(True),BooleanLiteral(False)))))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_59(self):
        input = r"""
procedure foo();
begin
    a[1+2] := foo(bar(), "hi", 3.4, -6.5)[4 And then trUE + FalsE] := "ahihi! hic hic";
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(Id(r'a'),BinaryOp(r'+',IntLiteral(1),IntLiteral(2))),StringLiteral(r'ahihi! hic hic')),Assign(ArrayCell(CallExpr(Id(r'foo'),[CallExpr(Id(r'bar'),[]),StringLiteral(r'hi'),FloatLiteral(3.4),UnaryOp(r'-',FloatLiteral(6.5))]),BinaryOp(r'andthen',IntLiteral(4),BinaryOp(r'+',BooleanLiteral(True),BooleanLiteral(False)))),StringLiteral(r'ahihi! hic hic'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_60(self):
        input = r"""
procedure foo();
begin
    a := -1.2+4.6*6 mod 7+m-f*k>4+2*5-6 div abc - - - 4 or 3 and then nhyil or else True;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'orelse',BinaryOp(r'andthen',BinaryOp(r'>',BinaryOp(r'-',BinaryOp(r'+',BinaryOp(r'+',UnaryOp(r'-',FloatLiteral(1.2)),BinaryOp(r'mod',BinaryOp(r'*',FloatLiteral(4.6),IntLiteral(6)),IntLiteral(7))),Id(r'm')),BinaryOp(r'*',Id(r'f'),Id(r'k'))),BinaryOp(r'or',BinaryOp(r'-',BinaryOp(r'-',BinaryOp(r'+',IntLiteral(4),BinaryOp(r'*',IntLiteral(2),IntLiteral(5))),BinaryOp(r'div',IntLiteral(6),Id(r'abc'))),UnaryOp(r'-',UnaryOp(r'-',IntLiteral(4)))),IntLiteral(3))),Id(r'nhyil')),BooleanLiteral(True)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_61(self):
        input = r"""
procedure foo();
begin
    a := b := c := d := e := f := g := faLSE;
    g := -1.2+4.6*6 mod 7+m-f*k>4+2*5-6 div abc - - - 4 or 3 and then nhyil or else True;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BooleanLiteral(False)),Assign(Id(r'b'),BooleanLiteral(False)),Assign(Id(r'c'),BooleanLiteral(False)),Assign(Id(r'd'),BooleanLiteral(False)),Assign(Id(r'e'),BooleanLiteral(False)),Assign(Id(r'f'),BooleanLiteral(False)),Assign(Id(r'g'),BooleanLiteral(False)),Assign(Id(r'g'),BinaryOp(r'orelse',BinaryOp(r'andthen',BinaryOp(r'>',BinaryOp(r'-',BinaryOp(r'+',BinaryOp(r'+',UnaryOp(r'-',FloatLiteral(1.2)),BinaryOp(r'mod',BinaryOp(r'*',FloatLiteral(4.6),IntLiteral(6)),IntLiteral(7))),Id(r'm')),BinaryOp(r'*',Id(r'f'),Id(r'k'))),BinaryOp(r'or',BinaryOp(r'-',BinaryOp(r'-',BinaryOp(r'+',IntLiteral(4),BinaryOp(r'*',IntLiteral(2),IntLiteral(5))),BinaryOp(r'div',IntLiteral(6),Id(r'abc'))),UnaryOp(r'-',UnaryOp(r'-',IntLiteral(4)))),IntLiteral(3))),Id(r'nhyil')),BooleanLiteral(True)))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_62(self):
        input = r"""
procedure foo();
begin
    for i := 1 to 10 do hic();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'hic'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_63(self):
        input = r"""
procedure foo();
begin
    for i := 1 doWntO 10 do hic();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),False,[CallStmt(Id(r'hic'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_64(self):
        input = r"""
procedure foo();
begin
    for i := a+2*c doWntO h(f+r*2) do hic();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),BinaryOp(r'+',Id(r'a'),BinaryOp(r'*',IntLiteral(2),Id(r'c'))),CallExpr(Id(r'h'),[BinaryOp(r'+',Id(r'f'),BinaryOp(r'*',Id(r'r'),IntLiteral(2)))]),False,[CallStmt(Id(r'hic'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_65(self):
        input = r"""
procedure foo();
begin
    for i := 1 to 10 do return;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[Return(None)])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_66(self):
        input = r"""
procedure foo();
begin
    for i := 1 to 10 do begin
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_67(self):
        input = r"""
procedure foo();
begin
    for i := 1 to 10 do begin
        ok();
        a := 4;
        return;
        break;
        continue;
        return hoho;
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'ok'),[]),Assign(Id(r'a'),IntLiteral(4)),Return(None),Break(),Continue(),Return(Id(r'hoho'))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_68(self):
        input = r"""
procedure foo();
begin
    while True do gogo();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[While(BooleanLiteral(True),[CallStmt(Id(r'gogo'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_69(self):
        input = r"""
procedure foo();
begin
    while True do return;
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[While(BooleanLiteral(True),[Return(None)])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_70(self):
        input = r"""
procedure foo();
begin
    while True do begin end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[While(BooleanLiteral(True),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_71(self):
        input = r"""
procedure foo();
begin
    while Foo() do begin end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[While(CallExpr(Id(r'Foo'),[]),[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_72(self):
        input = r"""
procedure foo();
begin
    while false do begin 
        ok();
        a := 4;
        return;
        break;
        continue;
        return hoho;
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[While(BooleanLiteral(False),[CallStmt(Id(r'ok'),[]),Assign(Id(r'a'),IntLiteral(4)),Return(None),Break(),Continue(),Return(Id(r'hoho'))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_73(self):
        input = r"""
procedure foo();
begin
    with i: integer; do ok();
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'i'),IntType())],[CallStmt(Id(r'ok'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_74(self):
        input = r"""
procedure foo();
begin
    with i: integer; do begin end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'i'),IntType())],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_75(self):
        input = r"""
procedure foo();
begin
    with i,j,k: integer; do begin end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'k'),IntType())],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_76(self):
        input = r"""
procedure foo();
begin
    with i,j,k: integer; 
        g: String;
        h,p,t: BooLean;
    do begin
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'k'),IntType()),VarDecl(Id(r'g'),StringType()),VarDecl(Id(r'h'),BoolType()),VarDecl(Id(r'p'),BoolType()),VarDecl(Id(r't'),BoolType())],[])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_77(self):
        input = r"""
procedure foo();
begin
    with i: real;
    do begin
        ok();
        a := 4;
        return;
        break;
        continue;
        return hoho;
    end
end
"""
        expect =str(Program([FuncDecl(Id(r'foo'),[],[],[With([VarDecl(Id(r'i'),FloatType())],[CallStmt(Id(r'ok'),[]),Assign(Id(r'a'),IntLiteral(4)),Return(None),Break(),Continue(),Return(Id(r'hoho'))])],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_78(self):
        input = r"""
var a: integer;
"""
        expect =str(Program([VarDecl(Id(r'a'),IntType())]))
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_79(self):
        input = r"""
var a, b, c: array[1 .. 2] of integer;
"""
        expect =str(Program([VarDecl(Id(r'a'),ArrayType(1,2,IntType())),VarDecl(Id(r'b'),ArrayType(1,2,IntType())),VarDecl(Id(r'c'),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_80(self):
        input = r"""
var a: array[1 .. 2] of integer;
    u, v: array[1 .. 2] of string;
"""
        expect =str(Program([VarDecl(Id(r'a'),ArrayType(1,2,IntType())),VarDecl(Id(r'u'),ArrayType(1,2,StringType())),VarDecl(Id(r'v'),ArrayType(1,2,StringType()))]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_81(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_82(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_83(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_84(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_85(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_86(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_87(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_88(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_89(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_90(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_91(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_92(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_93(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_94(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_95(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_96(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_97(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_98(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_99(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_100(self):
        input = r"""

"""
        expect =str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 400))


#########################################################
######    REMEMBER: Comment before submit code    #######
#########################################################