append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_sync.U_DWC_usb3_sync_pulse_dbc_usb_reset.src_pulse_edge_r\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.csr_dbc_epinfo\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_csr.hst_reg_data_out[*]\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_bmu.sb2rl_dev_usb_inep_pkt_buff_avail[*]\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrm.m2bt_reg_wr_rdy\"\n"
append rv "\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.sm2rb_csr_epinfo\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_lsp.U_DWC_usb3_lsp_glue.r2ml_lsp_ok_u2_hst[*]\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrm.sp2bt_update_u2_pls[0]\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_csr.U_DWC_usb3_csr_dev.r2bl_rxfifoempty\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_csr.U_DWC_usb3_csr_dev.grxthrcfg_reg[29]\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.sm32rl_pcc_dbc_tx_idle\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_csr.r2bl_interrupts_ored[*]\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.m2rl_csr_epinfo\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_bmu.U_DWC_usb3_bmu_bcu.sr2bt_gmr_mcmdvalid_req\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_u3pwrdwn.U_DWC_usb3_u3rhb.\instport[*].U_DWC_usb3_u3rhb_prt .U_DWC_usb3_u3rhb_prtsm.pop\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_u3pwrdwn.U_DWC_usb3_u3rhb.\instport[*].U_DWC_usb3_u3rhb_prt .rh_dbc_en\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_u3pwrdwn.U_DWC_usb3_u3rhb.\instport[*].U_DWC_usb3_u3rhb_prt .U_DWC_usb3_u3link.U_DWC_usb3_u3link_lque.lqtc_lque_status[*]\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_u3pwrdwn.U_DWC_usb3_u3rhb.\instport[*].U_DWC_usb3_u3rhb_prt .U_DWC_usb3_u3link.U_DWC_usb3_u3link_lpent.lprp_pent_rstop\"\n"
append rv "\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrm.U_DWC_usb3_pwrm_sync.sm2bb_u2_prt0_state\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_bmu.U_DWC_usb3_bmu_bcu.r2bt_gmw_mcmdvalid_req\"\n"
append rv "cdc_attribute -unrelated \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_sync.U_DWC_usb3_bussync_ltdb_sub_state.s2d_tgl\" \"DWC_usb3.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_sync.U_DWC_usb3_bussync_csr_epinfo.s_data_new\"\n"
append rv "cdc_attribute -unrelated \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrm.sb2mb_csr_tx_deemph[*]\" \"DWC_usb3.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrm.sb2mb_csr_tx_margin[*]\"\n"
append rv "cdc_attribute -unrelated \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.r2m3t_load_ux_timer[*]\" \"DWC_usb3.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.r2m3t_tlc_dbc_cmd_request\"\n"
append rv "cdc_attribute -unrelated \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.U_DWC_usb3_u2pwrdwn.pie_tx_vld[*]\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.sm32rb_dbc_port_num[*]\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.pcc3_rx_idle[*]\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrdwn.r2m3l_config_u3e\"\n"
append rv "quasi_static -name \"${design_name}.U_DWC_usb3_noclkrst.U_DWC_usb3_pwrm.U_DWC_usb3_pwrm_csr.b2rl_port_status_change[*]\"\n"
append rv "\n"
