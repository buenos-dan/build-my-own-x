	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0	sdk_version 15, 4
	.globl	_fib                            ; -- Begin function fib
	.p2align	2
_fib:                                   ; @fib
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	str	x0, [sp, #16]
	ldr	x8, [sp, #16]
	subs	x8, x8, #2
	b.ge	LBB0_2
	b	LBB0_1
LBB0_1:
	ldr	x8, [sp, #16]
	stur	x8, [x29, #-8]
	b	LBB0_3
LBB0_2:
	ldr	x8, [sp, #16]
	subs	x0, x8, #1
	bl	_fib
	str	x0, [sp, #8]                    ; 8-byte Folded Spill
	ldr	x8, [sp, #16]
	subs	x0, x8, #2
	bl	_fib
	mov	x8, x0
	ldr	x0, [sp, #8]                    ; 8-byte Folded Reload
	add	x8, x0, x8
	stur	x8, [x29, #-8]
	b	LBB0_3
LBB0_3:
	ldur	x0, [x29, #-8]
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols
