import re

def extract_channels(bvh_hierarchy):
    # Regular expression to match channel data
    joint_pattern = re.compile(r'JOINT\s+([A-Za-z0-9]+)\s*{.*?CHANNELS\s+(\d+)\s+([A-Za-z0-9\s]+)', re.DOTALL)

    # Dictionary to hold joint names and their channel data
    channels = {}

    # Find all joint-channel definitions
    matches = joint_pattern.findall(bvh_hierarchy)

    for match in matches:
        joint_name = match[0]
        num_channels = int(match[1])  # Number of channels (not used directly)
        channel_names = match[2].split()  # List of channel names (e.g., Xposition, Yposition)

        # Store the channels under the joint name
        channels[joint_name] = channel_names

    return channels


# Your BVH Hierarchy data (as a string)
bvh_hierarchy_data = """
ROOT Hips
{
    OFFSET 0.00000 0.00000 0.00000
    CHANNELS 6 Xposition Yposition Zposition Zrotation Yrotation Xrotation 
    JOINT LHipJoint
    {
        OFFSET 0 0 0
        CHANNELS 3 Zrotation Yrotation Xrotation
        JOINT LeftUpLeg
        {
            OFFSET 1.85590 -1.73949 0.84976
            CHANNELS 3 Zrotation Yrotation Xrotation
            JOINT LeftLeg
            {
                OFFSET 2.36836 -6.50702 0.00000
                CHANNELS 3 Zrotation Yrotation Xrotation
                JOINT LeftFoot
                {
                    OFFSET 2.53268 -6.95849 0.00000
                    CHANNELS 3 Zrotation Yrotation Xrotation
                    JOINT LeftToeBase
                    {
                        OFFSET 0.15935 -0.43781 1.94506
                        CHANNELS 3 Zrotation Yrotation Xrotation
                        End Site
                        {
                            OFFSET 0.00000 -0.00000 1.00661
                        }
                    }
                }
            }
        }
    }
    JOINT RHipJoint
    {
        OFFSET 0 0 0
        CHANNELS 3 Zrotation Yrotation Xrotation
        JOINT RightUpLeg
        {
            OFFSET -1.68297 -1.73949 0.84976
            CHANNELS 3 Zrotation Yrotation Xrotation
            JOINT RightLeg
            {
                OFFSET -2.44709 -6.72334 0.00000
                CHANNELS 3 Zrotation Yrotation Xrotation
                JOINT RightFoot
                {
                    OFFSET -2.43843 -6.69953 0.00000
                    CHANNELS 3 Zrotation Yrotation Xrotation
                    JOINT RightToeBase
                    {
                        OFFSET -0.20854 -0.57295 2.02172
                        CHANNELS 3 Zrotation Yrotation Xrotation
                        End Site
                        {
                            OFFSET -0.00000 -0.00000 1.05594
                        }
                    }
                }
            }
        }
    }
    JOINT LowerBack
    {
        OFFSET 0 0 0
        CHANNELS 3 Zrotation Yrotation Xrotation
        JOINT Spine
        {
            OFFSET -0.01560 2.23971 -0.03712
            CHANNELS 3 Zrotation Yrotation Xrotation
            JOINT Spine1
            {
                OFFSET 0.05490 2.19225 -0.19086
                CHANNELS 3 Zrotation Yrotation Xrotation
                JOINT Neck
                {
                    OFFSET 0 0 0
                    CHANNELS 3 Zrotation Yrotation Xrotation
                    JOINT Neck1
                    {
                        OFFSET -0.12403 1.43168 0.27585
                        CHANNELS 3 Zrotation Yrotation Xrotation
                        JOINT Head
                        {
                            OFFSET 0.17855 1.46173 -0.32578
                            CHANNELS 3 Zrotation Yrotation Xrotation
                            End Site
                            {
                                OFFSET 0.07217 1.51590 -0.14537
                            }
                        }
                    }
                }
            }
        }
    }
}
"""

# Extract the channel data
channels = extract_channels(bvh_hierarchy_data)

# Print the extracted channels
for joint, channel_list in channels.items():
    print(f"{joint}: {channel_list}")
