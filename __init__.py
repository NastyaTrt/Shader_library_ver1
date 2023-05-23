bl_info = {
    "name": "Shader library ver1",
    "author": "Anastasia Tretyak",
    "version": (1, 0, 0),
    "blender": (3, 30, 0),
    "location": "View3D > UI",
    "description": "Library with materials",
    "warning": "",
    "wiki_url": "",
    "doc_url": "",
    "category": "Material",
}

import bpy

class basePanel(bpy.types.Panel):
    bl_label = "Shader library for all materials"
    bl_idname = "SHADER_PT_basePanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Shad Library V1'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "SELECT A SHADER *\\0.0/*")
        row = layout.row()
        row.label(text = "Water")
        row = layout.row()
        row.operator('shader.muddywater_operator')
        row.operator('shader.cracked_ice_operator')
        row = layout.row()
        row.label(text = "Rubber")
        row = layout.row()
        row.operator('shader.multicolored_transp_rubber_operator')
        row = layout.row()
        row.label(text = "Stones")
        row = layout.row()
        row.operator('shader.rock_mat1_operator')
        row = layout.row()
        row.label(text = "Glass")
        row = layout.row()
        row.operator('shader.frosted_glass')
        row = layout.row()
        row.operator('shader.fully_transp_glass')
        
        
        
            
        
        
# FIRST MATERIAL - MUDDY WATER
        
class shader_OperatorType_MuddyWater(bpy.types.Operator):
    bl_label = "Muddy Water"
    bl_idname = 'shader.muddywater_operator'
    
    #Creating a new Shader. Index 0 will have materials created by the addon. The changed materials will be named from 1. This is my way of organizing work, such designations are not mandatory.
    def execute(self, context):
        material_MuddyWater = bpy.data.materials.new(name = "Muddy Water 0")
        material_MuddyWater.use_nodes = True
        
        #Removing Principled BSDF shader
        material_MuddyWater.node_tree.nodes.remove(material_MuddyWater.node_tree.nodes.get('Principled BSDF'))
        
        
        #Adding Shaders
        material_output = material_MuddyWater.node_tree.nodes.get('Material Output')
        material_output.location = (400, 0)
        material_output.select = False
        
        
        general_Principled_BSDF = material_MuddyWater.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
        general_Principled_BSDF.location = (-600, 0)
        general_Principled_BSDF.inputs[9].default_value = 0
        general_Principled_BSDF.inputs[17].default_value = 1
        general_Principled_BSDF.inputs[0].default_value = (1, 1, 1, 1)
        general_Principled_BSDF.select = False
        
        
        
        bump_1 = material_MuddyWater.node_tree.nodes.new('ShaderNodeBump')
        bump_1.location = (-1100, -400)
        bump_1.inputs[0].default_value = 0.05
        bump_1.inputs[1].default_value = 0.02
        bump_1.select = False
        
        
        musgrave_Texture = material_MuddyWater.node_tree.nodes.new('ShaderNodeTexMusgrave')
        musgrave_Texture.location = (-1300, -400)
        musgrave_Texture.inputs[2].default_value = 230.5
        musgrave_Texture.select = False
        
        
        invert_Node = material_MuddyWater.node_tree.nodes.new('ShaderNodeInvert')
        invert_Node.location = (-900, -400)
        invert_Node.select = False
        
        
        light_Path = material_MuddyWater.node_tree.nodes.new('ShaderNodeLightPath')
        light_Path.location = (-400, 400)
        light_Path.select = False
        
    
        mix_Shader = material_MuddyWater.node_tree.nodes.new('ShaderNodeMixShader')
        mix_Shader.location = (300, 0)
        mix_Shader.select = False
        
        
        transparent_BSDF = material_MuddyWater.node_tree.nodes.new('ShaderNodeBsdfTransparent')
        transparent_BSDF.location = (-200, -100)
        transparent_BSDF.select = False
        
        
        
        principled_Volume = material_MuddyWater.node_tree.nodes.new('ShaderNodeVolumePrincipled')
        principled_Volume.location = (-200, -200)
        principled_Volume.inputs[0].default_value = (0.55201, 0.806952, 0.838799, 1)
        principled_Volume.inputs[4].default_value = 0.121
        principled_Volume.select = False

        
        #Connections
        material_MuddyWater.node_tree.links.new(musgrave_Texture.outputs[0], bump_1.inputs[2])
        material_MuddyWater.node_tree.links.new(bump_1.outputs[0], invert_Node.inputs[1])
        material_MuddyWater.node_tree.links.new(invert_Node.outputs[0], general_Principled_BSDF.inputs[22])
        material_MuddyWater.node_tree.links.new(general_Principled_BSDF.outputs[0], mix_Shader.inputs[2])
        material_MuddyWater.node_tree.links.new(transparent_BSDF.outputs[0], mix_Shader.inputs[1])
        material_MuddyWater.node_tree.links.new(light_Path.outputs[0], mix_Shader.inputs[0])
        material_MuddyWater.node_tree.links.new(mix_Shader.outputs[0], material_output.inputs[0])
        material_MuddyWater.node_tree.links.new(principled_Volume.outputs[0], material_output.inputs[1])
         
        bpy.context.object.active_material = material_MuddyWater
         
        return {'FINISHED'}
    
    
    
#////////////////////////////////////////////////////////////////////////    

# SECOND MATERIAL - multicolored transparent rubber
        
class shader_OperatorType_Mult_transp_rubber(bpy.types.Operator):
    bl_label = "Multicolored transp rubber"
    bl_idname = 'shader.multicolored_transp_rubber_operator'
    

    
    #Creating a new Shader. Index 0 will have materials created by the addon. The changed materials will be named from 1. This is my way of organizing work, such designations are not mandatory.
    def execute(self, context):
        material_MulticoloredTranspRubber = bpy.data.materials.new(name = "Multicolored Transparent Rubber 0")
        material_MulticoloredTranspRubber.use_nodes = True
        
        #Removing Principled BSDF shader
        material_MulticoloredTranspRubber.node_tree.nodes.remove(material_MulticoloredTranspRubber.node_tree.nodes.get('Principled BSDF'))
        
        
        #Adding Shaders
        material_output_2 = material_MulticoloredTranspRubber.node_tree.nodes.get('Material Output')
        material_output_2.location = (400, 100)
        material_output_2.select = False
        
        
        general_Principled_BSDF_2 = material_MulticoloredTranspRubber.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
        general_Principled_BSDF_2.location = (-100, 100)
        general_Principled_BSDF_2.inputs[9].default_value = 0.068
        general_Principled_BSDF_2.inputs[17].default_value = 1
        general_Principled_BSDF_2.inputs[18].default_value = 0.5
        general_Principled_BSDF_2.inputs[0].default_value = (1, 1, 1, 1)
        general_Principled_BSDF_2.select = False
        
        
        
        bump_1_2 = material_MulticoloredTranspRubber.node_tree.nodes.new('ShaderNodeBump')
        bump_1_2.location = (-800, 100)
        bump_1_2.inputs[0].default_value = 1
        bump_1_2.inputs[1].default_value = 1
        bump_1_2.select = False
        
        
        bright_Contrast_2 = material_MulticoloredTranspRubber.node_tree.nodes.new('ShaderNodeBrightContrast')
        bright_Contrast_2.location = (-600, 100)
        bright_Contrast_2.inputs[1].default_value = 1.56
        bright_Contrast_2.select = False
        
        
        hue_Sat_2 = material_MulticoloredTranspRubber.node_tree.nodes.new('ShaderNodeHueSaturation')
        hue_Sat_2.location = (-400, 100)
        hue_Sat_2.inputs[0].default_value = 0.64
        hue_Sat_2.inputs[2].default_value = 1.22

       
       

        
        #Connections
        material_MulticoloredTranspRubber.node_tree.links.new(bump_1_2.outputs[0], bright_Contrast_2.inputs[0])
        material_MulticoloredTranspRubber.node_tree.links.new(bright_Contrast_2.outputs[0], hue_Sat_2.inputs[4])
        material_MulticoloredTranspRubber.node_tree.links.new(hue_Sat_2.outputs[0], general_Principled_BSDF_2.inputs[0])
        material_MulticoloredTranspRubber.node_tree.links.new(general_Principled_BSDF_2.outputs[0], material_output_2.inputs[0])
        
         
        bpy.context.object.active_material = material_MulticoloredTranspRubber
         
        return {'FINISHED'}
    
    
    
#////////////////////////////////////////////////////////////////////////    

# THIRD MATERIAL - Stones for the cave or just rock

class shader_OperatorType_Rock_Mat1(bpy.types.Operator):
    bl_label = "Rock Mat 1"
    bl_idname = 'shader.rock_mat1_operator'
    
    #Creating a new Shader. Index 0 will have materials created by the addon. The changed materials will be named from 1. This is my way of organizing work, such designations are not mandatory.
    def execute(self, context):
        material_Rock1 = bpy.data.materials.new(name = "Rock 1 ver 0")
        material_Rock1.use_nodes = True
        
        
        #Removing Principled BSDF shader
        material_Rock1.node_tree.nodes.remove(material_Rock1.node_tree.nodes.get('Principled BSDF'))
        
        
        #Adding Shaders
        material_output_3 = material_Rock1.node_tree.nodes.get('Material Output')
        material_output_3.location = (1200, 0)
        material_output_3.select = False
        
        
        voronoi_tex_mat3 = material_Rock1.node_tree.nodes.new('ShaderNodeTexVoronoi')
        voronoi_tex_mat3.location = (-200, 0)
        voronoi_tex_mat3.voronoi_dimensions = '4D'
        voronoi_tex_mat3.feature = 'F2'
        voronoi_tex_mat3.distance = 'MANHATTAN'
        voronoi_tex_mat3.select = False
        
        
        texture_coord_mat3 = material_Rock1.node_tree.nodes.new('ShaderNodeTexCoord')
        texture_coord_mat3.location = (-800, 0)
        texture_coord_mat3.select = False
        
        
        noise_tex_mat3 = material_Rock1.node_tree.nodes.new('ShaderNodeTexNoise')
        noise_tex_mat3.location = (-600, 100)
        noise_tex_mat3.inputs[2].default_value = 6
        noise_tex_mat3.inputs[3].default_value = 15
        noise_tex_mat3.select = False
        
        
        mix_rgb_1_mat3 = material_Rock1.node_tree.nodes.new('ShaderNodeMixRGB')
        mix_rgb_1_mat3.location = (-400, 0)
        mix_rgb_1_mat3.blend_type = 'LINEAR_LIGHT'
        mix_rgb_1_mat3.inputs[0].default_value = 0.1
        mix_rgb_1_mat3.select = False
        
        
        mix_rgb_2_mat3 = material_Rock1.node_tree.nodes.new('ShaderNodeMixRGB')
        mix_rgb_2_mat3.location = (0, 200)
        mix_rgb_2_mat3.inputs[0].default_value = 0.1
        mix_rgb_2_mat3.select = False
        
        
        color_ramp_1_mat3 = material_Rock1.node_tree.nodes.new('ShaderNodeValToRGB')
        color_ramp_1_mat3.location = (300, 0)
        color_ramp_1_mat3.color_ramp.elements[0].color = (0.0953074, 0.0953074, 0.0953075, 1)
        color_ramp_1_mat3.color_ramp.elements[1].color = (0, 0, 0, 1)
        color_ramp_1_mat3.select = False
        
        
        color_ramp_2_mat3 = material_Rock1.node_tree.nodes.new('ShaderNodeValToRGB')
        color_ramp_2_mat3.location = (300, -250)
        color_ramp_2_mat3.color_ramp.elements[0].color = (0.0193823, 0.0193823, 0.0193824, 1)
        color_ramp_2_mat3.color_ramp.elements[1].color = (0.854992, 0.854992, 0.854993, 1)
        color_ramp_2_mat3.select = False
        
        
        
        bump_mat3 = material_Rock1.node_tree.nodes.new('ShaderNodeBump')
        bump_mat3.location = (350, -500)
        bump_mat3.inputs[0].default_value = 0.1
        bump_mat3.select = False
        
        
        
        displ_mat_3 = material_Rock1.node_tree.nodes.new('ShaderNodeDisplacement')
        displ_mat_3.location = (950, -100)
        displ_mat_3.inputs[2].default_value = 0.15
        displ_mat_3.select = False
                
       

                
        general_Principled_BSDF_mat3 = material_Rock1.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
        general_Principled_BSDF_mat3.location = (600, 0)
        general_Principled_BSDF_mat3.select = False
        
        

        
        #Connections
        material_Rock1.node_tree.links.new(texture_coord_mat3.outputs[3], noise_tex_mat3.inputs[0])
        material_Rock1.node_tree.links.new(texture_coord_mat3.outputs[3], mix_rgb_1_mat3.inputs[1])
        material_Rock1.node_tree.links.new(noise_tex_mat3.outputs[1], mix_rgb_1_mat3.inputs[2])
        material_Rock1.node_tree.links.new(mix_rgb_1_mat3.outputs[0], voronoi_tex_mat3.inputs[0])
        material_Rock1.node_tree.links.new(noise_tex_mat3.outputs[0], mix_rgb_2_mat3.inputs[1])
        material_Rock1.node_tree.links.new(voronoi_tex_mat3.outputs[0], mix_rgb_2_mat3.inputs[2])
        material_Rock1.node_tree.links.new(mix_rgb_2_mat3.outputs[0], color_ramp_1_mat3.inputs[0])
        material_Rock1.node_tree.links.new(mix_rgb_2_mat3.outputs[0], color_ramp_2_mat3.inputs[0])
        material_Rock1.node_tree.links.new(voronoi_tex_mat3.outputs[0], bump_mat3.inputs[2])
        material_Rock1.node_tree.links.new(voronoi_tex_mat3.outputs[0], displ_mat_3.inputs[0])
        material_Rock1.node_tree.links.new(color_ramp_1_mat3.outputs[0], general_Principled_BSDF_mat3.inputs[0])
        material_Rock1.node_tree.links.new(color_ramp_2_mat3.outputs[0], general_Principled_BSDF_mat3.inputs[9])
        material_Rock1.node_tree.links.new(bump_mat3.outputs[0], general_Principled_BSDF_mat3.inputs[22])
        material_Rock1.node_tree.links.new(general_Principled_BSDF_mat3.outputs[0], material_output_3.inputs[0])
        material_Rock1.node_tree.links.new(displ_mat_3.outputs[0], material_output_3.inputs[2])
         
        bpy.context.object.active_material = material_Rock1
         
        return {'FINISHED'}
    


#////////////////////////////////////////////////////////////////////////    

# FOURTH MATERIAL - cracked ice
        
class shader_OperatorType_Cracked_ice(bpy.types.Operator):
    bl_label = "Cracked ice"
    bl_idname = 'shader.cracked_ice_operator'
    
    #Creating a new Shader. Index 0 will have materials created by the addon. The changed materials will be named from 1. This is my way of organizing work, such designations are not mandatory.
    def execute(self, context):
        material_CrackedIce = bpy.data.materials.new(name = "Cracked ice 0")
        material_CrackedIce.use_nodes = True
        
        #Removing Principled BSDF shader
        material_CrackedIce.node_tree.nodes.remove(material_CrackedIce.node_tree.nodes.get('Principled BSDF'))
        
        
        #Adding Shaders
        material_output_4 = material_CrackedIce.node_tree.nodes.get('Material Output')
        material_output_4.location = (400, 100)
        material_output_4.select = False
        
        
        general_Principled_BSDF_4 = material_CrackedIce.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
        general_Principled_BSDF_4.location = (-100, 100)
        general_Principled_BSDF_4.inputs[0].default_value = (0.679541, 0.814846, 1, 1)
        general_Principled_BSDF_4.inputs[16].default_value = 1.310
        general_Principled_BSDF_4.inputs[17].default_value = 1
        general_Principled_BSDF_4.select = False
        
        
#///////
        
        bump_1_4 = material_CrackedIce.node_tree.nodes.new('ShaderNodeBump')
        bump_1_4.location = (-400, -300)
        bump_1_4.inputs[0].default_value = 0.06
        bump_1_4.inputs[1].default_value = 1
        bump_1_4.select = False
        
        
        
        bump_2_4 = material_CrackedIce.node_tree.nodes.new('ShaderNodeBump')
        bump_2_4.location = (-650, -400)
        bump_2_4.inputs[0].default_value = 0.2
        bump_2_4.inputs[1].default_value = 1
        bump_2_4.select = False


        
        color_Ramp_1_4 = material_CrackedIce.node_tree.nodes.new('ShaderNodeValToRGB')
        color_Ramp_1_4.location = (-600, 100)
        color_Ramp_1_4.color_ramp.elements[0].color = (0.0843761, 0.0843761, 0.0843762, 1)
        color_Ramp_1_4.color_ramp.elements[0].position = 0.433
        color_Ramp_1_4.color_ramp.elements[1].position = 0.77
        color_Ramp_1_4.select = False
        
        
        color_Ramp_2_4 = material_CrackedIce.node_tree.nodes.new('ShaderNodeValToRGB')
        color_Ramp_2_4.location = (-970, -300)
        color_Ramp_2_4.color_ramp.elements[0].color = (0.0152085, 0.0152085, 0.0152085, 1)
        color_Ramp_2_4.color_ramp.elements[0].position = 0.4
        color_Ramp_2_4.color_ramp.elements[1].color = (0.0843761, 0.0843761, 0.0843762, 1)
        color_Ramp_2_4.color_ramp.elements[1].position = 0.77
        color_Ramp_2_4.select = False

    
       
        noise_Tex_1_4 = material_CrackedIce.node_tree.nodes.new('ShaderNodeTexNoise')
        noise_Tex_1_4.location = (-1200, -200)
        noise_Tex_1_4.inputs[2].default_value = 4
        noise_Tex_1_4.inputs[3].default_value = 5
        noise_Tex_1_4.select = False
        
        #//////
        
        noise_Tex_2_4 = material_CrackedIce.node_tree.nodes.new('ShaderNodeTexNoise')
        noise_Tex_2_4.location = (-1200, 100)
        noise_Tex_2_4.inputs[2].default_value = 1
        noise_Tex_2_4.inputs[3].default_value = 15
        noise_Tex_2_4.inputs[4].default_value = 0.8
        noise_Tex_2_4.select = False
        
       
       
        text_Coordin_4 = material_CrackedIce.node_tree.nodes.new('ShaderNodeTexCoord')
        text_Coordin_4.location = (-1500, -200)
        text_Coordin_4.select = False
       


        
        #Connections
        material_CrackedIce.node_tree.links.new(text_Coordin_4.outputs[3], noise_Tex_1_4.inputs[0])
        material_CrackedIce.node_tree.links.new(text_Coordin_4.outputs[3], noise_Tex_2_4.inputs[0])
        material_CrackedIce.node_tree.links.new(noise_Tex_1_4.outputs[0], color_Ramp_1_4.inputs[0])
        material_CrackedIce.node_tree.links.new(noise_Tex_1_4.outputs[0], color_Ramp_2_4.inputs[0])    
        material_CrackedIce.node_tree.links.new(color_Ramp_1_4.outputs[0], general_Principled_BSDF_4.inputs[9]) 
        material_CrackedIce.node_tree.links.new(color_Ramp_2_4.outputs[0], bump_2_4.inputs[2])  
        material_CrackedIce.node_tree.links.new(bump_2_4.outputs[0], bump_1_4.inputs[3])   
        material_CrackedIce.node_tree.links.new(noise_Tex_2_4.outputs[0], bump_1_4.inputs[2]) 
        material_CrackedIce.node_tree.links.new(bump_1_4.outputs[0], general_Principled_BSDF_4.inputs[22]) 
        
        material_CrackedIce.node_tree.links.new(general_Principled_BSDF_4.outputs[0], material_output_4.inputs[0])
        
         
        bpy.context.object.active_material = material_CrackedIce
        
                
        return {'FINISHED'}
    
    
    
    
#/////////////////////////////////////////////


# The Fifth Material - frosted glass
        
class shader_OperatorType_Frosted_glass(bpy.types.Operator):
    bl_label = "Frosted glass"
    bl_idname = 'shader.frosted_glass'
    

    
    #Creating a new Shader. Index 0 will have materials created by the addon. The changed materials will be named from 1. This is my way of organizing work, such designations are not mandatory.
    def execute(self, context):
        material_Frosted_glass = bpy.data.materials.new(name = "Frosted glass 0")
        material_Frosted_glass.use_nodes = True
        
        #Removing Principled BSDF shader
        material_Frosted_glass.node_tree.nodes.remove(material_Frosted_glass.node_tree.nodes.get('Principled BSDF'))
        
        
        #Adding Shaders
        material_output_5 = material_Frosted_glass.node_tree.nodes.get('Material Output')
        material_output_5.location = (500, 100)
        material_output_5.select = False
        
        
        mix_Shader_5 = material_Frosted_glass.node_tree.nodes.new('ShaderNodeMixShader')
        mix_Shader_5.location = (250, 100)
        mix_Shader_5.select = False
        
        
        glass_BSDF_5 = material_Frosted_glass.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass_BSDF_5.location = (0, 100)
        glass_BSDF_5.inputs[1].default_value = 0.4
        glass_BSDF_5.inputs[2].default_value = 1.33
        glass_BSDF_5.select = False
        
        
        transp_BSDF_5 = material_Frosted_glass.node_tree.nodes.new('ShaderNodeBsdfTransparent')
        transp_BSDF_5.location = (0, -100)
        transp_BSDF_5.inputs[0].default_value = (1, 1, 1, 1)
        transp_BSDF_5.select = False
        
        
        math_Maximum_5 = material_Frosted_glass.node_tree.nodes.new('ShaderNodeMath')
        math_Maximum_5.location = (0, 300)
        math_Maximum_5.operation = 'MAXIMUM'
        math_Maximum_5.select = False
        
        
        
        
        light_Path_5 = material_Frosted_glass.node_tree.nodes.new('ShaderNodeLightPath')
        light_Path_5.location = (-200, 300)
        light_Path_5.select = False

        
            
        #Connections
        material_Frosted_glass.node_tree.links.new(light_Path_5.outputs[5], math_Maximum_5.inputs[0])
        material_Frosted_glass.node_tree.links.new(light_Path_5.outputs[11], math_Maximum_5.inputs[1])
        material_Frosted_glass.node_tree.links.new(math_Maximum_5.outputs[0], mix_Shader_5.inputs[0])
        material_Frosted_glass.node_tree.links.new(glass_BSDF_5.outputs[0], mix_Shader_5.inputs[1])
        material_Frosted_glass.node_tree.links.new(transp_BSDF_5.outputs[0], mix_Shader_5.inputs[2])
        material_Frosted_glass.node_tree.links.new(mix_Shader_5.outputs[0], material_output_5.inputs[0])
        
         
        bpy.context.object.active_material = material_Frosted_glass
         
        return {'FINISHED'}
    
    
    
#//////////////////////////////////////////////////////////////////////// 

# Sixth material - fully transparent glass
        
class shader_OperatorType_Fully_transp_glass(bpy.types.Operator):
    bl_label = "Fully transp glass"
    bl_idname = 'shader.fully_transp_glass'
    

    
    #Creating a new Shader. Index 0 will have materials created by the addon. The changed materials will be named from 1. This is my way of organizing work, such designations are not mandatory.
    def execute(self, context):
        material_Fully_transp_glass = bpy.data.materials.new(name = "Fully transparent glass 0")
        material_Fully_transp_glass.use_nodes = True
        
        #Removing Principled BSDF shader
        material_Fully_transp_glass.node_tree.nodes.remove(material_Fully_transp_glass.node_tree.nodes.get('Principled BSDF'))
        
        
        #Adding Shaders
        material_output_6 = material_Fully_transp_glass.node_tree.nodes.get('Material Output')
        material_output_6.location = (500, 100)
        material_output_6.select = False
        
        
        mix_Shader_1_6 = material_Fully_transp_glass.node_tree.nodes.new('ShaderNodeMixShader')
        mix_Shader_1_6.location = (200, 100)
        mix_Shader_1_6.select = False
        
        mix_Shader_2_6 = material_Fully_transp_glass.node_tree.nodes.new('ShaderNodeMixShader')
        mix_Shader_2_6.location = (-100, -30)
        mix_Shader_2_6.select = False
        
        
        glossy_BSDF_6 = material_Fully_transp_glass.node_tree.nodes.new('ShaderNodeBsdfGlossy')
        glossy_BSDF_6.location = (-400, -300)
        glossy_BSDF_6.select = False
        
        
        fresnel_6 = material_Fully_transp_glass.node_tree.nodes.new('ShaderNodeFresnel')
        fresnel_6.location = (-400, -100)
        fresnel_6.inputs[0].default_value = 40000
        fresnel_6.select = False

        
        transp_BSDF_6 = material_Fully_transp_glass.node_tree.nodes.new('ShaderNodeBsdfTransparent')
        transp_BSDF_6.location = (-400, -500)
        transp_BSDF_6.inputs[0].default_value = (1, 1, 1, 1)
        transp_BSDF_6.select = False
        
        
        math_add_1_6 = material_Fully_transp_glass.node_tree.nodes.new('ShaderNodeMath')
        math_add_1_6.location = (-400, 100)
        math_add_1_6.operation = 'ADD'
        math_add_1_6.select = False
        
        
        math_add_2_6 = material_Fully_transp_glass.node_tree.nodes.new('ShaderNodeMath')
        math_add_2_6.location = (-600, 200)
        math_add_2_6.operation = 'ADD'
        math_add_2_6.select = False
        
    
            
        light_Path_6 = material_Fully_transp_glass.node_tree.nodes.new('ShaderNodeLightPath')
        light_Path_6.location = (-800, 100)
        light_Path_6.select = False

        
            
        #Connections
        material_Fully_transp_glass.node_tree.links.new(light_Path_6.outputs[1], math_add_2_6.inputs[0])
        material_Fully_transp_glass.node_tree.links.new(light_Path_6.outputs[2], math_add_2_6.inputs[1])
        material_Fully_transp_glass.node_tree.links.new(light_Path_6.outputs[3], math_add_1_6.inputs[1])
        material_Fully_transp_glass.node_tree.links.new(math_add_2_6.outputs[0], math_add_1_6.inputs[0])
        material_Fully_transp_glass.node_tree.links.new(fresnel_6.outputs[0], mix_Shader_2_6.inputs[0])
        material_Fully_transp_glass.node_tree.links.new(transp_BSDF_6.outputs[0], mix_Shader_2_6.inputs[2])
        
        material_Fully_transp_glass.node_tree.links.new(glossy_BSDF_6.outputs[0], mix_Shader_2_6.inputs[1])
        
        material_Fully_transp_glass.node_tree.links.new(mix_Shader_2_6.outputs[0], mix_Shader_1_6.inputs[1])
        
        material_Fully_transp_glass.node_tree.links.new(transp_BSDF_6.outputs[0], mix_Shader_1_6.inputs[2])
        
        material_Fully_transp_glass.node_tree.links.new(math_add_1_6.outputs[0], mix_Shader_1_6.inputs[0])
        
        material_Fully_transp_glass.node_tree.links.new(mix_Shader_1_6.outputs[0], material_output_6.inputs[0])
        
         
        bpy.context.object.active_material = material_Fully_transp_glass
         
        return {'FINISHED'}
       
    

         
        
def register():
    bpy.utils.register_class(basePanel)
    bpy.utils.register_class(shader_OperatorType_MuddyWater)
    bpy.utils.register_class(shader_OperatorType_Mult_transp_rubber)
    bpy.utils.register_class(shader_OperatorType_Rock_Mat1)
    bpy.utils.register_class(shader_OperatorType_Cracked_ice)
    bpy.utils.register_class(shader_OperatorType_Frosted_glass)
    bpy.utils.register_class(shader_OperatorType_Fully_transp_glass)


def unregister():
    bpy.utils.unregister_class(basePanel)
    bpy.utils.unregister_class(shader_OperatorType_MuddyWater)
    bpy.utils.unregister_class(shader_OperatorType_Mult_transp_rubber)
    bpy.utils.unregister_class(shader_OperatorType_Rock_Mat1)
    bpy.utils.unregister_class(shader_OperatorType_Cracked_ice)
    bpy.utils.unregister_class(shader_OperatorType_Frosted_glass)
    bpy.utils.unregister_class(shader_OperatorType_Fully_transp_glass)





if __name__ == "__main__":
    register()
