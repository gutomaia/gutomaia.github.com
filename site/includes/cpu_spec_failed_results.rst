.. csv-table::
   :header: Instruction, ApplePy,Arbne,JSnes,Py3NES,Py65,Pyntendo,6502js

   adc immediate with bcd,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:green:`OK`,:green:`OK`,:green:`OK`
   bcc,:green:`OK`,:red:`NOT`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`
   beq,:green:`OK`,:green:`OK`,:red:`NOT`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`
   bne,:green:`OK`,:green:`OK`,:red:`NOT`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`
   brk,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:green:`OK`,:green:`OK`,:green:`OK`
   irq interrupt,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`
   jsr,:red:`NOT`,:red:`NOT`,:red:`NOT`,:green:`OK`,:red:`NOT`,:green:`OK`,:red:`NOT`
   jsr stack pointer,:red:`NOT`,:green:`OK`,:red:`NOT`,:green:`OK`,:red:`NOT`,:green:`OK`,:red:`NOT`
   jsr with illegal opcode,:red:`NOT`,:green:`OK`,:green:`OK`,:red:`NOT`,:green:`OK`,:red:`NOT`,:red:`NOT`
   nmi interrupt,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`
   php,:green:`OK`,:green:`OK`,:red:`NOT`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`
   pla,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:red:`NOT`
   pla n flag set,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:red:`NOT`
   pla z flag set,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:red:`NOT`
   plp,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`
   rst interrupt,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`,:red:`NOT`
   rti,:green:`OK`,:green:`OK`,:red:`NOT`,:green:`OK`,:green:`OK`,:green:`OK`,:red:`NOT`
   rts,:green:`OK`,:green:`OK`,:red:`NOT`,:green:`OK`,:green:`OK`,:green:`OK`,:red:`NOT`
   sbc immediate with bcd,:red:`NOT`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`
   tsx,:green:`OK`,:green:`OK`,:red:`NOT`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`
   txs,:green:`OK`,:green:`OK`,:red:`NOT`,:green:`OK`,:green:`OK`,:green:`OK`,:green:`OK`
