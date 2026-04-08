#
# Copyright © 2021 Google, Inc.
#
# SPDX-License-Identifier: MIT

from freedreno_dev_info import *

# ----------------------------------------------------------------------
# БАЗОВАЯ КОНФИГУРАЦИЯ ДЛЯ A8XX (LRZ отключён, предзагрузка включена)
# ----------------------------------------------------------------------
a8xx_base = GPUProps(
        has_gmem_fast_clear = True,
        has_hw_multiview = True,
        has_fs_tex_prefetch = True,
        has_sampler_minmax = True,
        has_astc_hdr = True,
        prim_alloc_threshold = 0x7,
        vs_max_inputs_count = 32,
        max_sets = 8,
        instr_cache_size = 127,
        supports_multiview_mask = True,
        has_z24uint_s8uint = True,
        tess_use_shared = True,
        storage_16bit = True,
        storage_8bit = True,
        has_tex_filter_cubic = True,
        has_separate_chroma_filter = True,
        has_sample_locations = True,
        has_lpac = True,
        has_getfiberid = True,
        has_movs = True,
        has_dp4acc = True,
        has_lrz_dir_tracking = True,
        has_lrz_feedback = True,
        has_per_view_viewport = True,
        line_width_min = 1.0,
        line_width_max = 127.5,
        has_scalar_alu = True,
        has_scalar_predicates = True,
        has_coherent_ubwc_flag_caches = True,
        has_isam_v = True,
        has_ssbo_imm_offsets = True,
        has_early_preamble = True,
        has_attachment_shading_rate = True,
        has_ubwc_linear_mipmap_fallback = True,
        supports_linear_mipmap_threshold_in_blocks = True,
        prede_nop_quirk = True,
        predtf_nop_quirk = True,
        has_sad = True,
        has_bin_mask = True,
        has_sel_b_fneg = True,
        has_pred_bit = True,
        has_pc_dgen_so_cntl = True,
        has_eolm_eogm = True,
        has_dp2acc = False,
        has_rt_workaround = False,
        supports_double_threadsize = False,
        has_dual_wave_dispatch = True,
        has_salu_int_narrowing_quirk = True,
        reg_size_vec4 = 96,
        sysmem_vpc_pos_buf_size = 65536,
        sysmem_vpc_bv_pos_buf_size = 32768,
        has_event_write_sample_count = True,
        load_inline_uniforms_via_preamble_ldgk = True,
        load_shader_consts_via_preamble = True,
        has_gmem_vpc_attr_buf = True,
        ubwc_unorm_snorm_int_compatible = True,
        supports_uav_ubwc = True,
        has_generic_clear = True,
        r8g8_faulty_fast_clear_quirk = True,
        gs_vpc_adjacency_quirk = True,
        ubwc_all_formats_compatible = True,
        has_compliant_dp4acc = True,
        ubwc_coherency_quirk = True,
        has_persistent_counter = True,
        has_64b_ssbo_atomics = True,
        has_primitive_shading_rate = True,
        has_ray_intersection = False,
        has_sw_fuse = False,
        has_alias_rt = True,
        sysmem_vpc_attr_buf_size = 196608,            # 192 KB 
        gmem_vpc_attr_buf_size = 65536,              # 64 KB 
        gmem_vpc_pos_buf_size = 32768,                # 32 KB
        gmem_vpc_bv_pos_buf_size = 32768,             # 32 KB 
        disable_gmem = False,
        has_abs_bin_mask = True,
        new_control_regs = True,
        has_hw_bin_scaling = True,
        has_image_processing = True,
       
    )

# ----------------------------------------------------------------------
# КОНФИГУРАЦИЯ ДЛЯ A825 (GMEM 2МБ, CCU 128/128, VPC увеличены)
# ----------------------------------------------------------------------
a825 = GPUProps(
        gmem_size = 2 * 1024 * 1024,
        gmem_ccu_color_cache_fraction = CCUColorCacheFraction.HALF.value,
        gmem_per_ccu_color_cache_size = 128 * 1024,
        gmem_ccu_depth_cache_fraction = CCUColorCacheFraction.HALF.value,
        gmem_per_ccu_depth_cache_size = 128 * 1024,
        sysmem_ccu_color_cache_fraction = CCUColorCacheFraction.FULL.value,
        sysmem_per_ccu_color_cache_size = 128 * 1024,
        sysmem_ccu_depth_cache_fraction = CCUColorCacheFraction.THREE_QUARTER.value,
        sysmem_per_ccu_depth_cache_size = 96 * 1024,
        # VPC буферы – увеличены для устранения микрофризов
        sysmem_vpc_attr_buf_size = 196608,            # 192 KB 
        gmem_vpc_attr_buf_size = 65536,              # 64 KB 
        gmem_vpc_pos_buf_size = 32768,                # 32 KB
        gmem_vpc_bv_pos_buf_size = 32768,             # 32 KB 
        disable_gmem = False,
        enable_lrz_fast_clear = True,          # отключаем LRZ – убираем микрофризы
        enable_tp_ubwc_flag_hint = True,        # включаем для стабильности текстур
        shading_rate_matches_vk = True,
    )

# ----------------------------------------------------------------------
# MAGIC REGS (A8XX)
# ----------------------------------------------------------------------
a8xx_magic_regs = dict()

a8xx_raw_magic_regs = [
        [A6XXRegs.REG_A8XX_GRAS_BIN_FOVEAT_XY_FDM_OFFSET + 0, 0x00000000],
        [A6XXRegs.REG_A8XX_GRAS_BIN_FOVEAT_XY_FDM_OFFSET + 1, 0x00000000],
        [A6XXRegs.REG_A8XX_GRAS_BIN_FOVEAT_XY_FDM_OFFSET + 2, 0x00000000],
        [A6XXRegs.REG_A8XX_GRAS_BIN_FOVEAT_XY_FDM_OFFSET + 3, 0x00000000],
        [A6XXRegs.REG_A8XX_GRAS_BIN_FOVEAT_XY_FDM_OFFSET + 4, 0x00000000],
        [A6XXRegs.REG_A8XX_GRAS_BIN_FOVEAT_XY_FDM_OFFSET + 5, 0x00000000],
        [A6XXRegs.REG_A8XX_RB_RESOLVE_CNTL_5, 0x00000001],
        [A6XXRegs.REG_A8XX_SP_UNKNOWN_AB23,   0x00000000],
        [A6XXRegs.REG_A8XX_PC_UNKNOWN_980B,   0x00800280],
        [A6XXRegs.REG_A8XX_PC_MODE_CNTL,      0x00003f00],
    ]
# ----------------------------------------------------------------------
# РЕГИСТРАЦИЯ GPU
# ----------------------------------------------------------------------
add_gpus([
        GPUId(chip_id=0x44030000, name="Adreno (TM) 825"),
    ], A6xxGPUInfo(
        CHIP.A8XX,
        [a8xx_base, a825],
        num_ccu = 4,
        num_slices = 2,
        tile_align_w = 64,
        tile_align_h = 32,
        tile_max_w = 16384,
        tile_max_h = 16384,
        num_vsc_pipes = 32,
        cs_shared_mem_size = 32 * 1024,
        wave_granularity = 2,
        fibers_per_sp = 128 * 2 * 16,
        magic_regs = a8xx_magic_regs,
        raw_magic_regs = a8xx_raw_magic_regs,
    ))

if __name__ == "__main__":
    main()
