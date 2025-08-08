def build_prompt(company_name, target_industry, goal, product_description, tone):
    """
    Builds a comprehensive prompt for GPT-4o to generate cold emails.
    
    Args:
        company_name (str): The name of the company sending the email
        target_industry (str): The industry being targeted
        goal (str): The purpose of the email (sales, hiring, fundraising, etc.)
        product_description (str): What the company offers
        tone (str): The desired tone (Professional, Casual, Bold)
    
    Returns:
        str: Formatted prompt for GPT-4o
    """
    
    # Define tone-specific instructions
    tone_instructions = {
        "Professional": "Use formal business language, be respectful and courteous",
        "Casual": "Use friendly, conversational tone, be approachable and relatable",
        "Bold": "Use confident, assertive language, be direct and compelling"
    }
    
    tone_instruction = tone_instructions.get(tone, "Use professional but friendly language")
    
    return f"""
You are a world-class cold email copywriter with expertise in {goal} outreach.

Write a compelling cold email for a company called "{company_name}" targeting the {target_industry} industry.

CONTEXT:
- Company: {company_name}
- Target Industry: {target_industry}
- Email Goal: {goal}
- What they offer: {product_description}
- Tone: {tone_instruction}

REQUIREMENTS:
- Keep it to 3 short paragraphs maximum
- Start with a strong hook that grabs attention
- Include specific value proposition
- End with a clear, actionable call-to-action
- Make it personal and relevant to the target industry
- Avoid generic language and fluff
- Include a subject line that's compelling and relevant

FORMAT:
Subject: [Write a compelling subject line]

[Email body in 3 paragraphs]

The email should be ready to send immediately and optimized for high response rates.
""" 